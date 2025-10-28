# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98693436-f048-3765-aaab-546634c8370d | -10.6469 | -48.01538 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c70dd886-fa08-39db-ada9-b72bc5d0bd77 | -14.53055 | -47.99553 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ff475d5-9bd6-30e5-aaf2-243ea503169b | -10.56627 | -49.80363 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b6e03f7-662c-3ae6-adc8-8cad7238cd2c | -13.31707 | -48.34697 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78db1740-b433-3933-8ba7-d8f5e6ea7048 | -9.14444 | -51.302 | 2025-10-28 04:44:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c4772db-41ea-3486-82b0-e3c2b77854e5 | -9.22287 | -46.37006 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 18aa2998-5538-3e4a-8131-6cec7fba97c8 | -12.5305 | -47.54203 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 555af264-ef5c-3c9f-aa65-dfb464f539f1 | -12.40544 | -44.71509 | 2025-10-28 04:44:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac965308-fd8b-30f2-a127-6f21d1a79668 | -10.5607 | -49.79549 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c90cc2f2-89bf-345c-8230-140d5de2691c | -14.41202 | -47.91858 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2a13bde-e025-3b79-8318-10db15ff4382 | -10.92149 | -47.81412 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71adfb48-a644-37d0-8e15-dc72b3202d85 | -8.96697 | -50.18517 | 2025-10-28 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2098ef6b-30ae-3279-9197-6d15b6dc2d4c | -9.59693 | -46.85884 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a640b83-2043-304c-abdb-fb7bb373aad4 | -9.20169 | -47.18966 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9f55919-e26f-3c12-9530-06144aaa2391 | -15.22774 | -47.94946 | 2025-10-28 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91f28436-6f98-3be2-9b09-a4f5c7c7014d | -10.52423 | -47.72862 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f9840dc-47ca-314f-a7c0-84831f2302e6 | -13.3965 | -48.51558 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c073b92a-5055-300a-a074-394b5cd73b91 | -12.08768 | -45.67618 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75d9ad0e-900d-3424-8504-d1c56dc7ef16 | -13.35725 | -47.39371 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7479a5c-48a5-3289-a64a-82f1ada3b96e | -14.81498 | -46.71202 | 2025-10-28 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 020fe702-f3bf-374c-9f10-62b9b9ed50ea | -13.57453 | -48.53063 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a894bd2c-6002-3723-b415-59b3dc00a511 | -13.74013 | -48.40354 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9e7428b-cf3c-3597-8e9d-7c0ad15a502b | -10.87015 | -44.4138 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e1df863-97cd-38ea-9c0a-77b01dd4e51f | -9.89201 | -44.89874 | 2025-10-28 04:44:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d5ca128-2be8-37b8-9f9f-f10a9e790cda | -10.91114 | -50.25604 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf05bdf7-e663-395c-abaa-4099ac4b2c5f | -10.93072 | -47.9946 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2eb79c12-051a-3370-baab-93e05470212b | -14.81571 | -46.70679 | 2025-10-28 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6eb301e-d02c-33b3-b88e-6faa47711e50 | -11.71454 | -44.44249 | 2025-10-28 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33bcc3e5-8b34-36b3-a5dd-627a5cd6e35f | -13.56489 | -49.56464 | 2025-10-28 04:44:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4afc6b0-65a2-38e0-b702-9502d6b65dd1 | -14.62264 | -48.41823 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e254f44-0fba-3fe5-b247-b79201027480 | -10.73403 | -49.78628 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3ec8adca-d84d-3788-bd8e-55094e402b3c | -12.08659 | -45.65397 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e40c380f-5943-3f00-b45c-f0c1f7551ca3 | -10.75517 | -49.78238 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcda55de-f961-3c81-9d01-8bc1a46aaa09 | -13.2452 | -47.97026 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10d5f29f-a2b5-3d6b-945c-02a74132a59d | -10.92223 | -50.27225 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9552a40c-0638-3a2c-9241-c7d9e3ac0e50 | -13.61208 | -47.02936 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dac6e791-70a7-306f-8689-42a5b1441517 | -14.81449 | -46.70834 | 2025-10-28 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fcbdc0bf-6364-34c3-bca4-92084d6df2f5 | -9.55392 | -46.92208 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 902ea412-371a-36bc-b54b-c8f022ca7b89 | -9.95761 | -47.08521 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 436a2204-522c-36e7-8b06-7599e83fb62e | -10.91391 | -50.2601 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be8886ec-3deb-3697-9949-ffa4af6e37d8 | -10.56348 | -49.79956 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b2bfb27-bf78-38af-abe6-4c433763f1dd | -10.92833 | -50.2552 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a177e2b-1b4b-38b9-9e1c-da4cb414a78a | -12.54982 | -44.93262 | 2025-10-28 04:44:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36b9ab42-15a4-39c1-8fec-be181c43f939 | -13.92334 | -48.43387 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 373ec5d0-8215-3d27-b710-50f2b64718e3 | -13.2385 | -48.56289 | 2025-10-28 04:44:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b5844b8-855e-3568-b86d-8a7e53905b11 | -10.92833 | -50.27684 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71191a70-2e01-340b-b5c6-c3079ed2ba2c | -14.5579 | -47.98706 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02cc1c96-01e1-3eb9-99af-a52288b17758 | -15.20328 | -47.2154 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fee21cf5-d9dd-366d-9084-edd4c4e64e33 | -13.2458 | -47.96605 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45beae8f-8d42-3937-96ea-f13aa9af3827 | -9.06273 | -46.94811 | 2025-10-28 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d3041453-7d54-32b2-95ae-9a23de6d4cd3 | -15.1994 | -47.21505 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b6bdec4-36b7-314a-aa2d-c957a4c069cf | -13.93756 | -47.75073 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99509f78-d831-3104-868f-0f791ce8bd08 | -10.90718 | -48.00765 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9bc97128-0d9d-3c8f-a6f9-350f485c7dce | -10.12498 | -47.70455 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 755f0b86-3162-3b46-83c5-e57cbec0a4cf | -14.50527 | -47.89095 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7642b28-d666-320b-9127-1d36c7330be8 | -14.29797 | -44.52954 | 2025-10-28 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3f7e6a1-519f-3a90-8661-fee0a0419f3f | -9.98028 | -47.15756 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93dfcafc-a58c-3c8c-9f58-d4cefbe3a16b | -12.21945 | -46.52965 | 2025-10-28 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52f8c74a-d0c5-3558-b79b-c9c3d09b4659 | -13.77723 | -48.49685 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43dc0103-d670-342c-a04a-3e7132d9b7fc | -12.70014 | -46.31607 | 2025-10-28 04:44:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dac97f21-cef9-3333-bdb0-5c4eacc9a4a1 | -13.37658 | -43.46115 | 2025-10-28 04:44:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27212c36-49cb-3e4b-afa3-cf1dc043aee7 | -14.53115 | -47.99131 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82ac1915-58f3-3049-977c-720e29abee00 | -14.42598 | -49.42659 | 2025-10-28 04:44:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f8e9686-6728-3ca0-9c8a-a3cc68178d70 | -11.92969 | -47.66003 | 2025-10-28 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7230545-f1d8-36b3-9ab2-758eacf07ad4 | -10.78776 | -49.25974 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ac39e9b-e87e-3784-8f6f-6118417b1b63 | -13.26269 | -47.87376 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bc148cb-ecac-3460-9a51-0747f02d2c56 | -12.18857 | -47.01717 | 2025-10-28 04:44:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b98c58a-8b1a-365c-b0c9-5c181b6bd47e | -10.84355 | -47.8814 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38330ffd-e615-3ea4-862c-4af70e292644 | -13.91978 | -48.43335 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1fb2afa-75eb-39be-8bdf-a6684230fd3c | -11.80122 | -52.50233 | 2025-10-28 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ec55a4e-0392-32d4-b8d2-6d1a94c3787f | -13.30694 | -47.69411 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7d8b9a0a-62fc-33ec-a093-d4800fd5333a | -10.94777 | -50.27599 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc8919c1-a91f-330c-8499-a56daad56bbe | -13.26507 | -47.73105 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 372519ea-c33f-3950-be04-7dc6ff779030 | -8.34654 | -46.88932 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c01d7fc-62e8-32c8-8e1d-fd2ea3ab7500 | -9.46674 | -46.88468 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0862850-1e64-3339-b503-51012b0e6394 | -14.65075 | -48.40128 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 905c1ca6-f747-3b57-af73-47aef6755356 | -9.60505 | -45.19583 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1709c487-1094-3f68-a3eb-e9b2f8e8c62c | -9.46279 | -47.72672 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c95847bd-c8bc-3948-bcd4-ba0b5f5252a9 | -10.76185 | -49.78345 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14e35544-5278-3b2c-b5e2-6e2db9b8e1ac | -15.2253 | -47.94004 | 2025-10-28 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79977c8b-2080-3fbe-8ebd-e3d34cad6b4d | -9.55757 | -46.92262 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83e55686-23d5-32a1-beb6-942e3ee4dcde | -14.42313 | -49.42218 | 2025-10-28 04:44:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79fb8aac-9524-3022-9d60-4db218c4d919 | -9.21493 | -46.34601 | 2025-10-28 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e85e4718-dd28-39e1-b53b-d753279ec438 | -9.46219 | -47.73063 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c40bed4-74ad-3f59-a174-216b5c0880ed | -14.76742 | -44.9652 | 2025-10-28 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e49a7dd-ca24-3494-9b87-83208349cc30 | -10.56125 | -49.79196 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abe351e1-995c-37e1-affb-6278c4d5057b | -9.6093 | -47.78308 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 288b744f-9197-30e0-aab0-0d0f9c6b878d | -13.63478 | -47.034 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e8572247-9f9a-358f-aaba-f3d3b0c6a238 | -9.99251 | -48.10947 | 2025-10-28 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e97228fa-0d13-3549-bab8-b41680274c3a | -12.20358 | -46.50277 | 2025-10-28 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81577855-3e52-36fd-8495-bc2e2b3baf2d | -13.78432 | -48.49786 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6906a5db-7640-3d14-9c34-a0294fedb425 | -8.05873 | -54.93143 | 2025-10-28 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cbd55a4b-b903-36ca-ab03-8a5d0f9d5868 | -9.95459 | -47.08048 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 234701f3-7c74-350f-a980-0c7b58ebd28b | -15.15484 | -46.58766 | 2025-10-28 04:44:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc88b70e-94c5-3dce-9ce2-69c087495ec0 | -10.84003 | -47.88079 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96c1975b-54d6-3a69-8579-785a71c16de7 | -10.89381 | -50.08366 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baad657a-8eb2-323d-bfa5-96caf836503b | -10.90961 | -44.93802 | 2025-10-28 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe7c7241-1cb2-3a24-b8a0-a98e8d49d638 | -10.59448 | -47.95851 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eea05921-18e3-3816-8c5e-384d3a09ff14 | -13.18462 | -48.44016 | 2025-10-28 04:44:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed90a7d6-8f31-346d-86e3-126b9c55984f | -8.63725 | -45.2798 | 2025-10-28 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README62.md)
