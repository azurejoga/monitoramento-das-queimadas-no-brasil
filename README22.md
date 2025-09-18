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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 077dbe21-1095-30d0-acca-2d2544ae94c8 | -8.59127 | -45.72984 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa83c585-db9a-3ad3-bd0a-4d057c0ac50b | -8.78004 | -45.99191 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 876bd9fb-7ceb-36a7-8837-1636d73da263 | -7.38355 | -47.04472 | 2025-09-18 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a278251-02ca-3985-baab-7823cedbfad5 | -11.67712 | -50.50189 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03dd3316-7f88-34a7-9686-258b3851a7ba | -11.17691 | -45.36041 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d6ea966-06bc-3427-81d1-46c69ab7b657 | -14.26915 | -44.80059 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73746faa-3083-3387-854d-2c972f264c8e | -12.41068 | -44.72066 | 2025-09-18 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b07bbb96-d72e-3566-b4d8-bd83cfa3009f | -12.09639 | -44.8172 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 748b32aa-d169-38d5-9fa0-8e6b6a3a98ae | -7.57415 | -44.75523 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d852a8ec-0ab8-379d-9a0c-8d16e2f1cd86 | -11.50292 | -43.60357 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 302a5b15-9cf1-3d67-8c46-850947e76530 | -6.72407 | -47.20489 | 2025-09-18 04:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a572e9ec-c41b-33a3-af94-b7efc901dc11 | -14.31576 | -45.15082 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 999bffc7-93ae-3cf9-8962-139c1f8139fa | -12.08606 | -45.81177 | 2025-09-18 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2793bedd-f7a4-3508-bd5e-8c58499d2512 | -9.07125 | -47.01933 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0442f6df-e1f1-315f-a8ba-cd21d4623c84 | -8.13685 | -46.75352 | 2025-09-18 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf365526-31e5-36dd-a56a-39cdea97c1d5 | -7.44958 | -42.6258 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74937c21-c977-3c98-a699-95b511e57a18 | -7.53895 | -44.71627 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39a2b06c-569b-3beb-a2d8-2094482be016 | -10.91299 | -47.84547 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c858588-0d1f-3402-a1cb-a159162228f4 | -7.20677 | -44.3771 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0eddc53-fb5b-3569-91a0-edcfd0ed511a | -11.37194 | -50.8332 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 32754d17-47c9-3d63-a543-3c4d88bd3749 | -8.83564 | -43.01221 | 2025-09-18 04:14:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0bf67d5-926e-3a5c-be67-8025e772d975 | -7.98661 | -45.67668 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be632442-7732-31c0-bd89-771743e93f0c | -12.09356 | -44.83487 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbfa6c9b-3ed1-33cb-b9cf-e7fadafec6cc | -7.54489 | -44.76511 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 386b845b-2ffa-3d65-aa4b-7c1812b44717 | -11.16366 | -45.33599 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 330b8ebd-22d7-3fa4-93a8-fe2b878e643c | -9.19021 | -47.06999 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c26b284b-30ef-3c5f-bd4e-d7869d7acfbd | -8.48529 | -45.10944 | 2025-09-18 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c84ece1b-6ace-3020-a3d8-10bc54ce56a2 | -12.4118 | -44.71362 | 2025-09-18 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eaffa0a-466a-3e7d-a0cd-f41c11fd53ea | -9.11797 | -44.85575 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 769d8c3c-5a86-3ca2-b5dd-4817ef2c4137 | -8.13168 | -43.64546 | 2025-09-18 04:14:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a728805-21ac-340a-b76c-50f8814b4e07 | -7.80328 | -48.39078 | 2025-09-18 04:14:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc3eea85-7ae1-354e-86da-8f1cd2bb6239 | -7.20672 | -45.3346 | 2025-09-18 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08709ad9-435a-3dee-9fe3-e09a2437cb8f | -13.04387 | -47.97138 | 2025-09-18 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 91a36a14-f48a-306f-9018-1329d4d754dc | -7.86037 | -45.60907 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 503d70b0-bf44-3125-beba-2d45854b60d8 | -11.99594 | -46.71886 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d512da2-ffd2-3f86-b048-55f25867a776 | -7.52545 | -45.29689 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abfe60db-a3ad-3cb4-92f3-93ec9888aae3 | -11.04872 | -44.78342 | 2025-09-18 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74849048-39ea-36d9-8b27-86ba710435dc | -7.55615 | -44.75964 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8aca7819-e63a-37d1-8eea-71888caedd3d | -8.78351 | -45.99249 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11c69a6f-39e0-3ea0-93e9-9283154d5d6b | -11.16249 | -45.34319 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13601931-0056-3645-a20d-c47dc237c753 | -12.3983 | -51.43665 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8d85b943-c6af-3742-b6e3-3cdd0b6dc12e | -8.00964 | -45.68805 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b1e34c1-b991-3e05-aaa1-aeb108c0e42b | -14.30103 | -47.11124 | 2025-09-18 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a750e271-83ec-37b5-9ca4-da982b9e11a2 | -11.23695 | -47.43356 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 762711d7-dcc1-3a4e-a168-e64985d86391 | -9.85922 | -46.43973 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c49962f1-faa3-3575-9f4a-0e3af2ff2f3c | -9.08157 | -46.93439 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7474bf3e-032b-3056-a2f2-7b828a16edc0 | -11.17822 | -45.33099 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6a56caf-038a-3a10-86c7-0d435f682af8 | -7.40633 | -50.01403 | 2025-09-18 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 56a8402c-fe0c-377f-930d-7d6e14bc53ba | -7.39731 | -50.01255 | 2025-09-18 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35796ea5-f124-3c43-961a-ed3de55536f9 | -11.16744 | -45.35512 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bab80a35-3ec9-3df8-9df4-0018d0102c6e | -13.79238 | -44.33359 | 2025-09-18 04:14:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9485b409-1b53-3c1a-b40a-bb4c8a14bc7d | -10.83693 | -42.80056 | 2025-09-18 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bbe7375-98f7-3c72-8d0a-41f43da4de3d | -14.31189 | -45.15381 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 201a0197-b5fe-361a-bb2c-fbedf40b0bc2 | -7.45236 | -42.62983 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 92adb498-8dfa-3136-a05a-78d08128b2a8 | -7.69664 | -44.47747 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 649b19d7-8aac-3a8c-bd93-7c3fc1ca944d | -8.22063 | -41.18425 | 2025-09-18 04:14:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4fdcdac-cc48-3b5e-a9d4-5cb99fe7cfb4 | -7.44462 | -42.63578 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0fd19ab6-a817-3ec5-91df-da1e86459040 | -8.01616 | -44.94799 | 2025-09-18 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc20abfb-b95c-3f7d-bf79-04147a349fee | -7.59276 | -44.61788 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e9897e6-0da3-3d73-8e21-9703ca3d546c | -7.85787 | -46.11209 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90cf770c-c6d7-330b-9624-fad70d48765c | -8.83231 | -43.01168 | 2025-09-18 04:14:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| edf63f96-c172-31ea-803e-cafe892bdf73 | -8.90395 | -46.13971 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 483df08c-d1c8-33fb-9283-8c836e1fc03c | -8.88524 | -46.14428 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 096ecd2f-cebb-3452-b87e-cde1681e2946 | -13.70248 | -43.57323 | 2025-09-18 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08661ed9-ee50-308e-bc64-6baa9caf341d | -12.27212 | -45.2904 | 2025-09-18 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0199a6eb-618a-3244-a837-c59bf9e7a35a | -7.86162 | -45.6014 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 277d894f-7884-30f9-80a9-6b6bcc1a26a4 | -7.44185 | -42.63176 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0b9ebdae-4d34-36da-9939-c5b75310093c | -7.2168 | -44.37881 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76e9c388-0a9d-3657-8fdc-a45a949b9533 | -11.38278 | -50.83211 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 897efd3a-c158-3adc-b423-bf519812c86a | -10.52572 | -43.83998 | 2025-09-18 04:14:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3082e2a3-78dc-3e69-a8ca-2123ca3af83f | -14.46974 | -45.99314 | 2025-09-18 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 944c981c-bb34-350f-a3e1-550faa75e868 | -9.00736 | -48.17821 | 2025-09-18 04:14:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0cde7dd7-0866-3a2b-a1c3-c30d9e2954ec | -11.18595 | -45.34706 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f387222-f691-311b-8ab4-4c5af6908b3d | -9.14729 | -44.90102 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 39ef715f-89c0-31e7-b477-300c46572a5d | -8.65255 | -46.39325 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86cf160d-5ca5-3091-b4f1-6298e244364d | -8.9885 | -47.0433 | 2025-09-18 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f90d4fa6-fd2f-3800-b7d0-1fa0627ac5be | -7.52038 | -45.2847 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e26c1b3e-1434-3efb-8db0-90d052e64d94 | -7.8525 | -45.59209 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b07cfb1-ecb4-3dab-95b2-e2f521d35320 | -7.56649 | -49.57212 | 2025-09-18 04:14:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bacc46e1-81e2-3fe8-bd98-7e07b5613542 | -9.16283 | -46.94241 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 922c426c-930a-3566-8347-be812691138e | -7.66368 | -44.45374 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 848a4d99-4f7f-35c1-94bf-ef438473b9ea | -13.84793 | -44.90954 | 2025-09-18 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d75a301-ce0e-333b-bab8-6d79976bb793 | -10.64334 | -42.3071 | 2025-09-18 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6f47b1cf-dbdd-3151-86c5-838d97f9e058 | -12.09526 | -44.82426 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1176aae2-b323-324c-b4cd-ccda65dbd58c | -13.85536 | -43.99254 | 2025-09-18 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90223987-d739-307a-8016-04a607aad5d8 | -14.31851 | -45.15492 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 839bd8b1-504c-3af0-952a-01df4ff066a5 | -12.90201 | -44.66386 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8d729f6b-c630-31cc-ae32-486ed652097b | -8.00844 | -45.79359 | 2025-09-18 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04251e2f-91ba-313c-bd44-467031d7bd3e | -9.14786 | -44.89749 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3567ea78-f76e-3c3f-a583-56a314b2246d | -8.98773 | -45.74958 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e18dbe4-dbb2-32a2-a2dc-6aebf9b03cc4 | -7.32432 | -44.0017 | 2025-09-18 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cd9fee0-5092-361c-b154-a750ae78d035 | -7.53617 | -45.29459 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7458fabb-1d3a-3d12-b3a6-7abf871c079b | -8.01593 | -45.69314 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a31d902-5e18-384b-8ba2-0545db110660 | -14.47367 | -45.99009 | 2025-09-18 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ad288f8-45af-3a8f-a00c-6aa5a63c4191 | -7.40862 | -50.01169 | 2025-09-18 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ac21807-9363-3fd6-a1cc-f0561096d3e8 | -8.14703 | -46.75968 | 2025-09-18 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d98671e-b77e-3756-9d62-832b4ea747a7 | -12.10083 | -44.81066 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 780ab107-9cc9-32ad-9a50-0d9b70cbd432 | -13.22279 | -43.5202 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1986a55-a729-3e5a-a528-7027958cbd37 | -11.16526 | -45.34734 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3ddb09fe-4882-3e32-9646-b40ec70459a1 | -9.07679 | -44.94088 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README23.md)
