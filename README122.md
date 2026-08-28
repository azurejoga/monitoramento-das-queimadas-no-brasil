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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0856cda8-fea6-38ec-be55-799a6bd2f68a | -6.56635 | -56.54092 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a129c026-9eaa-33d4-a182-0c8a3b8e9068 | -3.73626 | -57.23577 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 419b09b4-d158-3574-9c85-b5e70a33443a | -11.49301 | -60.48171 | 2026-08-28 17:28:00 | NPP-375 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7f3e3652-d66d-3752-b8e7-d69a2e69a443 | -6.22535 | -55.48784 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a6b78eb9-cabf-3e86-9be8-3765c2bccfea | -6.06017 | -44.88424 | 2026-08-28 17:28:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8bfac93f-7d7e-3b7a-9fdd-c3642301c54f | -9.41903 | -50.44017 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 63ad382e-cf14-36c4-98a5-aab9a9a63e49 | -9.70251 | -65.08544 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| bb677d1c-581c-3df1-83eb-e2e3ff065780 | -8.58947 | -54.78298 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| ef16ed3b-6181-36b9-9ab5-083157334709 | -9.30874 | -56.79815 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d510e73a-6137-35a9-8632-b0dd648af872 | -6.59823 | -55.43938 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d1b0ce54-4ecf-3155-8b52-45398d3b91da | -7.91968 | -61.32104 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57cc028e-add9-39e9-bd36-561e7888bc12 | -7.58243 | -61.32998 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 69e62c21-1031-3315-9252-2ec348dd4b85 | -9.1012 | -59.41595 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 04be05aa-0d9e-3f12-8dc0-a9865e1c9118 | -8.9545 | -62.38127 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| d49c9037-9417-3f16-8c25-2b114e54d3cb | -6.95399 | -45.42779 | 2026-08-28 17:28:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1cf33cc3-2c7f-3ed4-b365-8ddc6a933513 | -9.25639 | -57.07748 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3a6bb772-6cc5-384d-b79c-ae221a78449d | -6.95941 | -59.4847 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 9b585da1-51e0-303e-bd17-3688af77664a | -7.93023 | -61.36649 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| c20be342-4cdf-3293-b087-efeb38133e7d | -9.25693 | -57.08103 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ce4f5c0a-0472-308e-8b20-061ceda5804b | -6.45511 | -43.08161 | 2026-08-28 17:28:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 29421f35-8e15-3a17-a795-d63809e418de | -6.8276 | -56.41711 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5e405d67-6c3a-31b4-920c-d3cfc9be4a3e | -6.70558 | -56.35074 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1829019e-0d62-370f-b4ac-6fa251811066 | -8.63762 | -66.53465 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 31e7b59a-fcd9-308f-b113-ec7e2b5f5220 | -8.61391 | -54.67593 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e57ec424-5fcd-346c-b060-9d4d5152bf44 | -6.21459 | -55.48573 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8618527f-a6ca-3e32-9022-d9a7d859b9ef | -7.04172 | -55.68562 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 7e809ddc-d68e-3a0c-8372-95d13ac23cec | -7.47893 | -61.38867 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 945f8093-bdf5-30a5-9abb-0c8bf5bb33ab | -6.15254 | -57.94633 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d81b14ef-de0a-3b5e-b8e1-b558c9617634 | -8.57069 | -64.17328 | 2026-08-28 17:28:00 | NPP-375 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 877e3fb7-06ee-34cf-ac28-be831a7be55b | -5.92038 | -61.30708 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d3ccaa38-e700-3105-8b35-2f262d03b088 | -7.58316 | -61.22261 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7efb3fe5-9808-3f5a-be1f-074f1e2dba35 | -7.50126 | -55.28065 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f18597f4-6779-3b83-9d97-a162541a7291 | -3.70422 | -45.25012 | 2026-08-28 17:28:00 | NPP-375 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 72601b04-bbbe-36ee-9440-03d5a20d4f41 | -7.276 | -49.85051 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1ddafc05-6fac-394f-aef8-22e6c52c8a95 | -6.59992 | -55.42795 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1b3472ab-7ff1-302e-97c0-33f08500fe51 | -6.16845 | -57.78841 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 15bae213-8429-39fd-93c4-18e4ef38a7be | -5.78965 | -57.60093 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8db4eb00-5b3c-3f7a-a59f-43273764f881 | -10.49846 | -64.49246 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 56de5e40-35d5-34ae-a011-57694ef0d305 | -2.72034 | -47.0507 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| de79f6a8-4c27-3cdf-a9bc-772d8f4d5504 | -6.86057 | -59.47079 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 256a1eae-857f-3403-807d-830b8f4c9062 | -6.65516 | -58.50438 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1ed2e343-ae68-366e-915b-3b46986d5fc5 | -6.66039 | -56.337 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 08d4c1c8-108a-3983-9d01-f2e2b448f16b | -3.17608 | -54.61663 | 2026-08-28 17:28:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| dea7420a-c68f-3f3c-aa2a-15b53da31b00 | -6.76074 | -55.6978 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 782f28ae-abf6-34be-a2f9-2b1e76c86727 | -10.51024 | -69.35008 | 2026-08-28 17:28:00 | NPP-375 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 0ba6efbd-2efd-391f-b7c1-00928674dbd5 | -7.59178 | -61.33894 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 2d30f6b6-c71a-3cec-ac5b-edbb7cd6df17 | -9.63384 | -48.26704 | 2026-08-28 17:28:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3e3f91a7-76fa-3e42-b00b-36e0ba1de002 | -3.766 | -57.98296 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 63a1f4c8-6859-3a8b-a0ce-ee2c770e92f6 | -9.70209 | -65.0822 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2163dc05-e7bc-3c6d-9568-654616e1b79c | -8.44434 | -70.70982 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 29.3 |
| d6b807ab-1dac-33dd-8be8-6d4b703a6049 | -7.62562 | -61.34954 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c65f3beb-eec9-336b-a5c5-8fa68a73a0eb | -9.24636 | -57.07903 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2a86d103-64f8-3c3a-8ad4-1ca7cb97973c | -9.24809 | -57.06787 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4294cc6b-be68-3fe6-a6cd-2db869016214 | -9.23324 | -51.52105 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2aa001d3-8f9e-3182-a6a1-134a20906020 | -5.88917 | -52.10731 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 53ba4aa0-0ea6-3e09-8a32-1ad38f47f52a | -5.97207 | -57.71551 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 4c22abd1-2026-360f-bb4a-611e4da22aad | -6.78193 | -59.42562 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| adeaca79-0e92-3a5c-b4f9-c8d79343725f | -9.6948 | -62.20827 | 2026-08-28 17:28:00 | NPP-375 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26aada17-50f3-3ea5-965f-5324f44753c4 | -6.21119 | -55.48624 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b55e512-99b5-31a6-9616-f2354a634097 | -6.17127 | -57.7844 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| be91c35c-b6cb-341c-83f0-904b2db09b97 | -7.04564 | -55.68867 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2b9432ff-5142-3ed6-9772-e544bf243ca5 | -4.4725 | -55.40797 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 13dc19c6-c233-3b22-8c69-4789a9d68398 | -2.72599 | -47.03063 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 4da2daff-3301-3052-8f4f-c9c23bc424e8 | -6.15149 | -56.10836 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 7b9cb1f2-8231-3688-88bc-f1884f72e7b0 | -8.5952 | -54.79729 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 37c52a4e-32d1-323d-a48c-db819e698d05 | -10.49296 | -64.49012 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 5a2015a4-6778-399f-ba5e-381fec36393d | -4.34421 | -55.43557 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e4e6e4a6-b233-3245-8a17-ab60eeb5fa83 | -6.75681 | -55.69474 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3033f74a-7c23-3800-9560-9b030dc569a7 | -9.11272 | -60.3072 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f6139e1f-030f-33b2-b03d-3fd81c1f04ec | -4.96534 | -44.89709 | 2026-08-28 17:28:00 | NPP-375 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| bb53bc21-ca9d-3059-9ea8-75405d3e06d7 | -5.48391 | -45.12257 | 2026-08-28 17:28:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9cda66b6-5c3d-3345-b482-e1cb3b9f344d | -6.57447 | -55.44309 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 32ae8f6a-4823-3bb1-ad0e-24a252e8d82f | -6.65462 | -58.50073 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0bb4c4e3-a985-323d-a30d-c6709b00d02e | -8.60438 | -54.83359 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 27838e5f-5d71-339e-bccb-9b1a19b2d1ea | -10.49258 | -64.48714 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c6ff48f5-404d-3a88-8e69-988303f353ed | -5.99963 | -57.82967 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 7acc1fbf-6126-3160-8da4-7568980bd93b | -8.93341 | -50.71417 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8920eb1-5759-3f44-80b9-238a552bbe06 | -7.59356 | -61.32319 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fd5ae7e1-1262-3c28-8cae-9a4e7025dabe | -4.74057 | -55.94514 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 46c87e47-9632-3900-b43a-3bdcb547400d | -10.39107 | -61.19928 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d9396230-19c2-391c-932d-2d862a95c707 | -5.88078 | -61.27883 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 45849c20-b320-3297-9b72-3af39ccc5771 | -4.31728 | -59.47783 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 22fb79f3-45e7-3500-b50f-7c7f21d1dc7f | -10.39301 | -61.24314 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a416927c-f130-3c26-b62e-6435f86f153a | -8.53805 | -70.62366 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c4e1b8e6-bd92-3f8a-b691-b2ad7028660a | -2.72355 | -47.03271 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| deabd821-821f-391d-ae7f-2044dbdae373 | -9.68837 | -65.10039 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9a603a53-f92b-350b-9ffd-47af415c27d6 | -6.82755 | -51.90111 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 95d988d1-b175-3e0e-ac05-f3e22b94e199 | -9.93413 | -60.44075 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| d3007ac3-c698-301f-aa03-e1b81f550965 | -2.92024 | -45.23529 | 2026-08-28 17:28:00 | NPP-375 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b0e6e294-ee62-3513-92cd-36e34a2d9100 | -8.15301 | -63.9978 | 2026-08-28 17:28:00 | NPP-375 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 02e74734-8753-353a-bd56-d882d5242783 | -9.10178 | -59.4165 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 65a67b5e-e8e3-3ddf-9a4d-4de0f70c8fba | -7.44463 | -50.92454 | 2026-08-28 17:28:00 | NPP-375 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8cc94c09-15d4-3f33-9467-f23ce424afe2 | -7.56063 | -57.73076 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd01489c-a3fe-3f86-895e-13822e139d87 | -10.75738 | -53.97821 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 59889c2b-e8ef-35de-a76b-0696ad51f2eb | -10.31627 | -68.4584 | 2026-08-28 17:28:00 | NPP-375 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 117c0538-db7f-38d8-85da-53f778c666e5 | -7.98621 | -45.50394 | 2026-08-28 17:28:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| af7756e9-6c18-3f67-b520-7416da03b56e | -7.36536 | -55.19009 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c26a406a-a079-3960-8bc8-21351e10bf31 | -9.25251 | -57.07444 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b05dc321-43ae-3d30-adee-84bd3df80691 | -7.24678 | -46.25 | 2026-08-28 17:28:00 | NPP-375 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cacaa58b-9ace-37d0-80c5-5a26558f7e9a | -7.56116 | -57.73431 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README123.md)
