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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcd09567-11a5-3119-b547-51ba2cd3de0e | -5.87522 | -53.64142 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 771116ce-9169-398e-9e8a-421edd0bf73f | -7.57814 | -57.68533 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be0af62b-bad1-3e23-a78f-29f5582ff1e6 | -6.79632 | -58.78799 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 337e59db-b13a-3c84-8e35-1d926ab23231 | -6.35069 | -57.77132 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d511b4bf-ed2e-3da7-9a1b-7327b8d3e3ba | -9.56411 | -66.02938 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 630029dc-24b0-3e72-8630-078904db7493 | -6.27995 | -56.03468 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3129c2b2-3bba-3eb7-b0ba-2dae0faf5705 | -7.24797 | -55.59208 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 174dcae4-9d61-3128-8cc9-87f409204f68 | -3.48116 | -59.58079 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39993a12-0c4c-3f67-bc6b-68d26ebd3a7c | -6.79532 | -59.94978 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5100c2e8-df08-30b8-96d2-ec4311f3a78b | -3.06721 | -61.271 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a73c1c64-3182-3f33-a328-5b0501e1c81f | -3.05929 | -54.40906 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9914f18a-b37d-3a6f-b684-d36b26cf4ed1 | -2.86071 | -60.91378 | 2026-09-22 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a45ae42-6600-338c-8583-ac5dd1de5812 | -6.61294 | -59.10239 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 021688c9-63d1-3908-9bb4-4ad49559d274 | -4.53654 | -54.97308 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddf37dbc-f88c-39af-8b67-cca79c023de5 | -3.94146 | -59.63806 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc86db2e-26fa-3ab9-a073-8e140e9db205 | -1.7489 | -47.13959 | 2026-09-22 05:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd015bad-3bd0-39ba-ac11-063a03e29622 | -7.61547 | -55.3545 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f01dd334-fe5a-3e4c-9f37-9aec9f109a11 | -4.21745 | -48.61685 | 2026-09-22 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b867efc0-ecc2-323e-b029-ef160a2c0c98 | -4.18456 | -49.41122 | 2026-09-22 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ead183b-de3c-32dd-8f1b-9645d1802155 | -4.22798 | -48.61556 | 2026-09-22 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c15db166-81ea-3734-a671-a6981abada08 | -10.15051 | -58.76392 | 2026-09-22 05:23:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff9aee0d-e66a-37b0-bdad-42b6e6d9d48d | -12.88836 | -50.93386 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f4035f54-f815-3291-8c77-7b1496d7db18 | -4.63961 | -55.77053 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b59b704-409a-395f-8f24-184079afa2a2 | -5.43453 | -60.23129 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d5ffc2d-0053-365d-8db9-49c3ba4bf854 | -6.05053 | -57.82383 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0183bf5e-2476-3598-a349-ec3ebc8aa1d1 | -4.26116 | -60.00991 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c38873b3-cf7f-3cae-9f08-22d27344225a | -3.24175 | -60.80655 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38ecb05c-d54d-38c2-80b6-fe9f638c2613 | -3.47252 | -59.53083 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 372d8190-87db-348f-be6d-9100eda77245 | -14.58324 | -52.16891 | 2026-09-22 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94232ac7-f893-3104-942a-a5a968953380 | -6.76165 | -59.11077 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47ddaf07-6102-395e-8b9c-e379e918d561 | -7.19552 | -46.55087 | 2026-09-22 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b668ce95-d218-3315-a7dc-504d839c52cc | -6.70006 | -59.95968 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| da879ad6-ce0c-3d2b-9be2-d85cac613a7e | -9.10818 | -65.3761 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 469465b3-b8cf-304b-b7a5-38c507d25cc7 | -5.20803 | -56.10213 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46ffb910-a08a-39ef-b767-7ef1a0cbf999 | -2.93824 | -50.49606 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 667d799f-dace-31e3-963d-30ba7e0e582c | -6.74653 | -59.07449 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b42174a0-45f1-3422-81b2-0e883589780c | -3.33064 | -59.81479 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87816fcd-4263-332b-aedd-fcf5c74734a8 | -6.78307 | -58.61301 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d68e8685-1cf0-3f1e-b965-d31fe623000a | -6.16755 | -57.70662 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1588170-eba6-395a-a6c1-2f6aa4a6e2bf | -6.1033 | -57.6216 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91b05b17-2c86-331c-9862-b99ab4f471af | -3.54356 | -58.68483 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39a4d974-d8cf-30c1-8a54-5420755d5f5d | -3.06277 | -54.4096 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b72660de-f431-36c8-b244-c551f635dfec | -4.66413 | -55.63548 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ddba903-76a0-3fe6-a8f0-5aec747d01ea | -6.30795 | -57.73953 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c509e4d-3378-3183-a946-5594c692349f | -5.80152 | -53.51909 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29f2f6a1-c138-3794-b6a0-2383528c6cd0 | -6.00177 | -57.70898 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbf67a33-7d2f-3a96-b427-8d9a220c40e0 | -2.86919 | -57.79272 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 33959bc9-9a25-3ffb-8815-b8f5dcf5205c | -13.34307 | -51.28275 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fde8173d-3826-398b-a35e-8cf8c895336b | -6.07834 | -57.62833 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aaffe237-346b-34df-bdd1-b3d95865b1d2 | -4.48087 | -55.48996 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e741312-2c65-3dbc-b19b-b6bc0724093d | -6.55247 | -56.25581 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3be0895-e009-3727-8a85-4df8cea6ae4f | -3.40714 | -61.29565 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69c197ce-5576-3450-b24c-a59a46d06a2f | -3.41829 | -61.29525 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f19cdc71-a25f-3223-9937-9c891171e575 | -6.29296 | -57.74785 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a63fd95-3392-380d-8712-7253d9e80b72 | -7.24364 | -55.58454 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f17ffe2c-c6ce-364e-8f70-35f3b17afca2 | -12.56003 | -45.96239 | 2026-09-22 05:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18ea8288-610f-341c-8571-cc9a5e6e7515 | -5.83053 | -53.5072 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9218c33c-4b69-3cd2-a662-77768d740e03 | -12.95428 | -50.9259 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 321c7548-d613-3db1-be94-06688d0886f2 | -2.52646 | -58.0819 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9522f7fe-2648-3aa9-82d4-1d69eb3cd228 | -7.72196 | -43.88567 | 2026-09-22 05:23:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d916158-b0aa-3a7a-8aa9-41895731cac4 | -4.2725 | -55.43886 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d7e47712-9bb9-3f3a-bfef-3f8b9a6a1ff6 | -9.09783 | -65.37943 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b5525f1-1b23-3a40-99ee-c9cca4d50579 | -7.58423 | -57.66845 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25811569-9748-3911-9000-a115e5f7e09a | -7.61198 | -55.35396 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20653150-0eed-35a2-abf6-967139ad6e16 | -6.30851 | -57.73605 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbbc60bc-ff5a-3e89-bd7b-5bc360ef3825 | -4.56189 | -54.9232 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be0d3f3d-212a-3792-891e-ff41ccd58b13 | -6.68945 | -58.45973 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edd9f5fd-a5ef-3d88-95b6-10e82c3c4c94 | -6.15518 | -57.955 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da16ccbc-6dd7-367f-88e6-bed55063123a | -5.10392 | -56.30572 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbe4f66c-6806-3696-b170-5103c0ddaf33 | -9.18519 | -65.85049 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07c466d3-1c40-37a9-8353-bce0f88bdc76 | -3.05582 | -54.40852 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b5aa889-8e4a-3058-82bd-8c0ccd52d121 | -4.22577 | -63.07823 | 2026-09-22 05:23:00 | NPP-375D | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0b7e68f-6881-3de3-8b9f-32a008575d6c | -5.83427 | -53.50778 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57718ff7-9755-3584-a8e7-59e577095e4a | -6.11272 | -59.88919 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a08a4a7-3aec-3e7d-a94f-042b59851a02 | -4.95943 | -55.82408 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30424444-86b2-3df6-aed0-d3b8132b86bd | -6.11886 | -57.75962 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aca2ca1f-6bb8-3ad4-82d7-0528bd2b1430 | -3.00451 | -54.18175 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8272f09-fee0-3f4c-850b-edde682c8fee | -9.67112 | -66.82567 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50ce6d60-b8dc-3449-9722-532724177de6 | -5.45899 | -60.15058 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01d6194b-7ab2-31b3-9513-e3c9823d7387 | -7.60849 | -55.35342 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cdd60ba-27c4-3e81-b7f1-dd14aec2c46a | -3.8731 | -51.18694 | 2026-09-22 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eca7662d-81a3-31ff-9af0-d36bb51220c8 | -3.71872 | -60.57714 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1fdfe020-c039-3ee0-9cb6-663638485b94 | -5.8883 | -52.04249 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad4c9f2d-7a74-3bb6-ba68-5f8111eacc22 | -11.24253 | -54.10915 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a48b2e33-8ff9-31ea-b6ab-26d1210cde9b | -2.95157 | -57.71814 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6ddf090-60d6-3a42-b4ab-5d2dd61753a5 | -5.85655 | -52.03034 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d81cd97e-40a0-3612-99fa-e5ea437318a6 | -3.718 | -60.58165 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 827dd9c8-9522-31a4-99d0-021b64ceff8c | -5.75185 | -57.53348 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a34f64d-97ea-3b98-9cc4-14a94b392017 | -11.03763 | -54.14853 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6817bbda-980f-34f6-abc0-9bd954f1bea1 | -7.56926 | -57.67677 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88e98c59-fca1-3073-8796-81d61cec0618 | -3.41698 | -60.20223 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b86566e-e0be-3a12-ab97-935714f4da39 | -3.45373 | -50.61423 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef8676db-f527-3473-9917-089f0fe17750 | -6.84213 | -55.53526 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a19d6737-84a9-39d3-8d90-46c4529f5c74 | -6.62209 | -57.97952 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9eae581-1ad1-3dc5-b781-36c4ec0b3062 | -3.0684 | -59.30586 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edb55d5f-656c-34dc-a5e2-f32e0d544553 | -6.44578 | -59.96843 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4633c2ce-395f-39dc-b4ca-fd78ce3efa15 | -4.49441 | -56.07428 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaf204fc-e5dd-3de1-8d6d-ec679f91dbeb | -7.58424 | -57.68987 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60ee31c2-d2e5-3938-86d8-5f37c55452b5 | -6.73547 | -55.07636 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee5682dd-18a9-3b53-9150-a1c8f426cfbf | -6.75476 | -56.3241 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README78.md)
