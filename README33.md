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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13bbe69c-81c3-3885-90e5-5a770d1fe8b9 | -11.59751 | -52.18122 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 56cc4cdf-27f9-350b-a2f0-ad267e455e01 | -10.76134 | -48.29519 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 680a826f-8401-316f-aad8-ba07a33b9751 | -13.75363 | -46.94036 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 596d5cef-18a8-3432-a6e3-4a165c85ffb0 | -11.91527 | -46.65047 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20b08fc1-690d-30c3-ae92-286aedd0816f | -9.07604 | -46.99456 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 449106da-990e-3c17-acb7-cb3ffaa2a577 | -11.98393 | -40.86596 | 2025-09-05 04:36:00 | NPP-375D | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 667c6506-8830-32fc-b21e-ef46fe34729d | -12.33 | -47.05234 | 2025-09-05 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 442ed032-4b0a-333c-8f10-df0e8c09c11b | -9.07492 | -47.00188 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| bf4099a2-5d76-3aeb-8350-ec822bfb07a5 | -10.88317 | -55.39413 | 2025-09-05 04:36:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ee502dd-04f8-3f53-b273-a5a188b1b1b8 | -7.82113 | -46.08976 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59efcac3-e4cc-3790-818a-ae1bb3889813 | -10.97856 | -46.00724 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84250310-ba9a-32df-b7c3-22b313eea77f | -8.97496 | -44.45589 | 2025-09-05 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82946e7c-d242-396c-ad16-0fca5c517087 | -12.27084 | -50.1598 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf7344dc-d9a3-31ee-b750-b8a27d341ca5 | -12.88736 | -48.02089 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b67dd561-d979-36e3-821c-73837d8a8ee4 | -10.76115 | -45.26504 | 2025-09-05 04:36:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 697a6855-c139-35b4-95d8-d52a8b927ffb | -9.81526 | -48.3072 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d62e66c9-6b57-3a39-8da5-720e42c74651 | -11.93167 | -46.66066 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8b4973a-9144-391c-a089-f3fff65396a8 | -8.85835 | -52.01705 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 484238be-613c-3519-9f5f-6e430a07bf78 | -10.96619 | -45.96764 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac370b61-e297-34cc-a5de-dbe9e3258181 | -9.07831 | -47.00237 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c15dec21-f482-3ce9-9ec6-41c9676676ea | -12.52035 | -48.0677 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd365e2b-0315-3dd8-9b43-04d4427611af | -12.71854 | -45.08603 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3aadca81-b85d-3d0e-a0b4-687c03546b22 | -11.20123 | -55.02131 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b1bc6ff-da30-34f5-b175-f4f94be0bd37 | -13.6609 | -47.92849 | 2025-09-05 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eaebb0b0-3566-3caf-bbcd-f6dadd5967db | -8.52692 | -51.30986 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba2471aa-ed5e-3c77-bede-1f69ae4719a9 | -9.69082 | -51.05301 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b711800e-9a24-3246-8e88-d6a90412d879 | -12.32076 | -47.04306 | 2025-09-05 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ae77450-a215-3937-b559-feb7c07f40c9 | -12.93749 | -48.05471 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3ad0505-73d4-3e65-a09e-67fccbc08e21 | -7.05996 | -50.86197 | 2025-09-05 04:36:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74e0a027-a282-307a-b122-4e60a152479e | -8.98054 | -44.449 | 2025-09-05 04:36:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b9e50ac-0857-3d36-8774-a347d95407ab | -10.10168 | -46.24039 | 2025-09-05 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61c59f77-e42a-3076-aa10-aaa1963470ed | -10.76418 | -45.27005 | 2025-09-05 04:36:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ce04ad1-32d6-3301-8cd0-1cc4667b3646 | -9.69435 | -51.05351 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01b259dc-6130-3faa-a3dd-71ccedd84b9c | -8.00818 | -45.44992 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f29e9242-ea5f-3173-bb5c-7ead9d7d2e9d | -13.55757 | -48.12804 | 2025-09-05 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 285fd416-908e-37a9-b903-7fd62cd85628 | -11.67401 | -57.34172 | 2025-09-05 04:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7aa085f-99d2-36d6-ab8c-a6bcab2f5828 | -12.26193 | -50.15091 | 2025-09-05 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b9ccc6a-ec5a-3fe3-a74e-b29e05a311ff | -10.07935 | -48.06788 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9272e14-1f5e-3b81-9dd5-b2f6ffd99def | -8.09829 | -45.3512 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a2dce41-fc61-34dc-8d1c-fa537793e996 | -5.49546 | -60.12784 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53dc3ada-9829-3124-930a-985bfc9cb3dd | -11.99104 | -46.7494 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42affb8a-49f6-33de-86fe-b0f6f7bc97da | -9.07264 | -46.99409 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6557d4c1-29e6-3e62-9dd8-c9461b0bf55a | -5.50868 | -60.13029 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c78a60d-23a0-3eb6-ba39-8471c6dfdb76 | -11.5837 | -52.10914 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e339a5b5-a739-3c0e-8687-541114743b29 | -11.38849 | -43.60603 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b3d89ff-3d3f-3c03-a0a6-803f205bc910 | -8.44131 | -45.04104 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f070a699-c655-3713-b64b-823633cca1f1 | -11.31801 | -55.22458 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7960d8e6-9646-3f7a-9d89-0fa21eb631cf | -12.8851 | -48.013 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68e92019-4ea6-3e22-994e-823b1a5566a0 | -9.50459 | -57.8236 | 2025-09-05 04:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6792521e-da7c-3d60-853f-be274bbbe4e2 | -13.29935 | -46.85007 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bf098d0-bab6-370f-be87-ebec6ae642d4 | -10.97639 | -45.9482 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59129d78-3a80-3464-a212-d88bcfc28f7e | -12.48673 | -48.08447 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 398aa131-841f-3ce5-b106-7bf2e6cb90ca | -7.76137 | -48.78831 | 2025-09-05 04:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cc7d9c1a-322a-3cb0-9ea4-5dcb229c6a82 | -11.63963 | -52.21925 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed51351c-a1c2-363f-acc8-d8875192b1ff | -8.07204 | -52.34737 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 91d1f9c4-fd28-363f-ad1a-43df1259a944 | -12.90703 | -48.02786 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e0def90f-d1ea-32f1-a129-94c369f80928 | -9.49986 | -57.81924 | 2025-09-05 04:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ada07a9-8b33-3df9-a75f-c470f8e2c69d | -8.07583 | -50.20282 | 2025-09-05 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf73c978-be9e-398a-a840-df72f66c28c4 | -14.55674 | -48.08603 | 2025-09-05 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4fbfa89-c11d-37cc-beec-efb21b6691e1 | -15.06202 | -50.07444 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57ffd987-92a3-3692-8e30-57ec2f91d3f4 | -15.01439 | -50.08167 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8dec14d-345f-3b25-b6c7-a43353e1d646 | -14.13598 | -51.71501 | 2025-09-05 04:38:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1eeb105-5bca-3851-bd4e-f024410e42d6 | -12.97132 | -54.78809 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ad41956-77f9-37ed-bde1-4df3554dffbe | -14.98614 | -50.06583 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7c5e7ab-7d76-328f-8385-a6d9d32a9022 | -12.97271 | -54.80404 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af646f1d-7911-3bb6-ba4b-9522f07fc972 | -16.32396 | -52.9601 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 87cd6358-c4bc-3538-b465-2447dcafe704 | -15.0412 | -50.04199 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98c0d1f8-a50e-3a48-8f48-fcb607f91c65 | -19.68771 | -54.80603 | 2025-09-05 04:38:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76dce748-37b3-37ec-9454-e82e2ff50acb | -15.05079 | -50.102 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2520405-7c34-37b8-bc51-53945ce721ea | -12.97752 | -54.80104 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce0ea28c-7bc2-3276-8d2f-f536167e008f | -21.49207 | -46.1889 | 2025-09-05 04:38:00 | NPP-375D | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2e28b368-5ac2-3443-b9a5-c8a704392c5c | -12.98924 | -54.80711 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 25e586d0-2333-3e13-8e01-c964c9072620 | -15.5455 | -48.41544 | 2025-09-05 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffbd504a-9407-32a3-98ee-8e7691b9888c | -12.98233 | -54.79805 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52ecfb64-9ba9-3c58-88cf-a65e0102c31e | -20.44624 | -43.95791 | 2025-09-05 04:38:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b9bf171-8f39-344b-ab01-c3a4b831a1ac | -12.98856 | -54.81089 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92b6aad3-1424-3bf9-9ff9-c2e5e496b405 | -15.1972 | -52.36438 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71bdd25f-3f28-3cf2-b9ba-1688bf8f65af | -15.99228 | -55.95088 | 2025-09-05 04:38:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 6ecc5f53-5718-35c6-b718-d995e7447603 | -12.97339 | -54.80024 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1809c132-064c-3f1c-b1c2-a7bbc34afd76 | -12.97888 | -54.7935 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10349d60-92a1-3f06-bdb0-9b30cde9234c | -15.85028 | -52.30371 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3014b730-efec-320f-ad7e-e6d6d80dd3f6 | -16.20295 | -49.33703 | 2025-09-05 04:38:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cdefd8f-2aa3-38e7-9fec-22ce5de5d507 | -17.96784 | -41.70927 | 2025-09-05 04:38:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| dfca163a-d7b7-3518-8faf-d1c00d344503 | -14.99327 | -50.08547 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e8f6a09-7bdb-3045-860b-0ecdb553b768 | -12.97544 | -54.78889 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c02b704c-d478-37a2-9022-2692db89a1a4 | -15.05869 | -50.07389 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4294ca00-55c9-364b-84e6-0cf7587be723 | -19.79023 | -43.55133 | 2025-09-05 04:38:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92384fdc-3e1d-30c0-8776-da1af4b20091 | -14.985 | -50.073 | 2025-09-05 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 245cfb98-a792-34fc-b881-cd2f443756d8 | -12.98305 | -54.81777 | 2025-09-05 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7696d474-9220-33c1-b9fa-69334c053b87 | -13.27446 | -51.8527 | 2025-09-05 04:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c73334a-11be-3a88-92df-4b83c8d09968 | -15.61805 | -52.90921 | 2025-09-05 04:38:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64c6e206-47c0-37b8-a230-d251898adb12 | -15.18464 | -51.16963 | 2025-09-05 04:38:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8421c141-46c4-34cd-b461-9a3b2eeb4292 | -15.56923 | -50.33242 | 2025-09-05 04:38:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2b4680b-cdbb-3714-9e89-77e43c101c08 | -16.30832 | -52.94447 | 2025-09-05 04:38:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 093eeabd-21de-3607-b0d6-36d33818841e | -14.28491 | -45.21923 | 2025-09-05 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 723b5301-44bc-3ac2-9878-9ff78bbce6f6 | -15.87 | -52.18559 | 2025-09-05 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d88c9484-801e-3d52-8e04-3abb87a8747f | -21.36554 | -46.95193 | 2025-09-05 04:38:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a58295a-19bf-3596-b867-dbc26e3b1664 | -14.75414 | -47.49176 | 2025-09-05 04:38:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86e4d8a4-cb6b-3430-ab60-9437e0ef45e5 | -19.67943 | -54.80913 | 2025-09-05 04:38:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 05b44667-5e75-30ed-9111-97622e9dbe4a | -16.44583 | -51.06585 | 2025-09-05 04:38:00 | NPP-375D | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README34.md)
