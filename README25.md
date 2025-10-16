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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f30ec06c-447e-35c1-a767-dc94199af576 | -6.44597 | -43.38457 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acb7d87d-2ad1-32a3-8215-348feeaeb71d | -7.60005 | -35.71634 | 2025-10-16 03:47:00 | NOAA-20 | AROEIRAS | PARAÍBA | Brasil | 2501302 | 25 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 940d53cc-f8ca-3193-beb7-72c548743ab4 | -3.8516 | -41.56802 | 2025-10-16 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3f0f5abc-b8da-360f-b021-34669a4d23e3 | -5.76625 | -47.91821 | 2025-10-16 03:47:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b72317e5-89c9-30a9-9693-6634d2260bb1 | -12.73848 | -43.46565 | 2025-10-16 03:47:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| faeca84b-3153-338d-83c8-ef4abb5188c2 | -11.06437 | -38.8378 | 2025-10-16 03:47:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d637a5b1-f865-33de-99db-20f255d2633a | -6.738 | -42.15226 | 2025-10-16 03:47:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f9fbcfa5-4fff-3cdd-9827-d975f246321c | -10.94864 | -43.08534 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb6f2e81-5b34-368c-99b0-0c4dc1112901 | -6.03862 | -41.93329 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a4737de7-67a3-3197-8fa9-5bafcdb57634 | -4.83253 | -45.66142 | 2025-10-16 03:47:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67ef8b3e-2d62-3c3f-8440-bac606776f43 | -10.66465 | -45.31062 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29d44b81-69c0-31aa-9bcf-28388d7495c8 | -6.1802 | -44.29485 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 322a4497-b528-394d-aea3-a9e9d37a8203 | -9.71756 | -44.51342 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 466c5869-1ad1-31e5-b605-00352a1190fe | -3.00985 | -45.39254 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ca7ee1a-dc97-3286-8335-14e23caf4a38 | -5.89314 | -44.27055 | 2025-10-16 03:47:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e79d012d-d985-3922-8afd-da8019024fc2 | -6.39713 | -41.49302 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| aeb5e1e0-caba-33de-9b36-05b054f8a2c7 | -10.65405 | -45.25666 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2742f924-ba03-3b32-8dae-b583af8ca64a | -3.28274 | -40.89339 | 2025-10-16 03:47:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ea42c685-2d5c-37cc-8cfa-edef2dfd81ee | -6.45263 | -43.37889 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd95a918-16bf-3e69-aa41-3b6a8b058400 | -6.39368 | -41.7905 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5462d192-f596-332e-8a96-2381eb6d92b8 | -12.66637 | -44.12659 | 2025-10-16 03:47:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3258995e-e397-3994-8d40-e836972d8dbe | -5.88261 | -42.78492 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d58a0fb5-c3fd-3127-b98a-ca27a18fefa0 | -5.93115 | -39.43483 | 2025-10-16 03:47:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f6a0843f-f16e-36c0-9a14-ed74c57fab5c | -6.04057 | -41.92196 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bb87121c-c6bc-3e20-aba7-82e9919e1076 | -1.38149 | -49.31096 | 2025-10-16 03:47:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98b8facf-7c8b-3674-9220-4bbd7e881d13 | -10.51109 | -43.3665 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9736c08-f917-3855-bfbe-c63ce3cdf037 | -5.05116 | -44.46708 | 2025-10-16 03:47:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75f354df-8941-37b3-9964-2db16d119ef7 | -4.38117 | -43.401 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4dde4e65-c920-3cbf-b57d-747e0bffb0a6 | -6.1737 | -41.78391 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 756e3865-4c08-384f-b7ef-5ebe31268025 | -10.07031 | -42.73492 | 2025-10-16 03:47:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d78e676-05da-3df6-ad58-14ac65cf5a35 | -6.04356 | -41.94198 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ec04add2-9bef-37d0-9e7f-9a219693c291 | -4.67045 | -44.10251 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e5df77d-fa2d-3bbd-88ee-71b2d33afbea | -6.05041 | -41.93909 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6c079463-d454-3535-9ed1-f694148b3cd3 | -4.76398 | -40.86739 | 2025-10-16 03:47:00 | NOAA-20 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 82ef56ee-dcfb-389b-b2f2-fd3522eebd2b | -2.44077 | -49.37986 | 2025-10-16 03:47:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03d87db2-f63d-3dcf-952e-de60ef476b84 | -9.16101 | -46.87378 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ace34cd-5133-3bd2-a12b-42633f3ea5c3 | -12.77551 | -43.30762 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29bae8f9-516b-3130-abf8-ee98fe77c73c | -5.879 | -43.89629 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad5aae8c-5a8d-3dcb-8c1d-c26773602fe9 | -5.73459 | -41.31406 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5183a994-5efb-3a2e-be8e-8f92aa5e704d | -5.51204 | -43.20487 | 2025-10-16 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e41f6704-9bcc-335e-aa36-8be57b6ff75b | -4.36101 | -43.39583 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7c2f32d7-da1d-3a91-bbe8-cc4251847edc | -5.87587 | -43.88602 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f036f948-21a1-3e00-ab1c-ddfac2e29a43 | -7.65889 | -34.98798 | 2025-10-16 03:47:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ce210d0a-4087-364a-a833-25970f629410 | -4.35903 | -46.78082 | 2025-10-16 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c0bdb3a-f5b1-3c2c-a799-cc4e46d66140 | -4.66371 | -44.11258 | 2025-10-16 03:47:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 476e393f-7b8b-3333-b191-5d66f02bef30 | -5.60572 | -44.25982 | 2025-10-16 03:47:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca19c5d9-3d7a-36f8-9e98-375830e6a5a6 | -6.04991 | -44.2488 | 2025-10-16 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 91d1fec4-06cf-34c2-a7d8-0255a57e8c11 | -3.59224 | -43.04649 | 2025-10-16 03:47:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20c98e96-5bab-30d5-85e6-698bc6fb6179 | -10.13518 | -44.54922 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47bc6fc6-c80e-3061-9c23-04153b6e9f62 | -5.42199 | -44.23197 | 2025-10-16 03:47:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcaabe45-8fff-3f26-9782-920976953c99 | -10.56955 | -44.83074 | 2025-10-16 03:47:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43ecccd8-393a-3cde-9228-d9051bed0684 | -5.79178 | -35.60074 | 2025-10-16 03:47:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 24e9f568-ec94-33bd-9491-c7173b392edd | -13.24014 | -40.94914 | 2025-10-16 03:47:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 698ec35d-2e49-347c-874c-16f9bf3ae849 | -4.91341 | -45.98363 | 2025-10-16 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f7e7bc30-c4c0-3107-a84c-f74acca7d038 | -4.9125 | -45.98384 | 2025-10-16 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b2aa8ce-1f6d-3fbd-bdb8-abaa3ec1d389 | -3.84108 | -44.54708 | 2025-10-16 03:47:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5b6510c-c160-3af7-84f5-8d09b154ffdb | -5.23489 | -42.01149 | 2025-10-16 03:47:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7da10ab6-d39b-35d0-a941-4a3566f6333c | -4.35678 | -45.53327 | 2025-10-16 03:47:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f3b3802-628b-3ee1-ae68-84876d1832fb | -6.46437 | -41.89154 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14612256-b243-32a4-9a47-49bb24471f4e | -10.05295 | -43.83154 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 43c8ecd4-39c8-3f8b-b118-95ecea359a49 | -10.72522 | -47.5932 | 2025-10-16 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b0604be-ccb4-3124-9808-60b497191e32 | -4.92165 | -41.55415 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b036878-fb76-3a10-931f-276fdb7c7af6 | -5.34143 | -41.21568 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 99395c3b-8061-3471-b966-1d02eb92912e | -5.65838 | -45.96504 | 2025-10-16 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de8ae30e-0db0-370e-bc31-17a870d846c3 | -10.65869 | -45.31138 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a7e1e4b-dbf7-3b5d-bd1d-14299e6633a3 | -12.66931 | -43.43334 | 2025-10-16 03:47:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 84013107-31eb-3e74-b069-a0e0d4f5f825 | -4.88524 | -46.71003 | 2025-10-16 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccd0c402-4122-3e77-9bf6-f361b0097f65 | -5.33375 | -45.03278 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a078914f-646f-3cae-a4ca-a96a41f2c039 | -11.45118 | -44.01123 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3dcc9f3-08dd-3683-9166-12aa7bd2064c | -5.38089 | -48.91758 | 2025-10-16 03:47:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0c7445c2-b008-3c54-bdbd-06f8903f6b98 | -4.38673 | -43.39675 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8539e940-3ef3-37c1-a54d-a0633dd127dd | -3.59339 | -48.8869 | 2025-10-16 03:47:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee404820-4fdf-3177-8bff-c72a3fc008ce | -4.93674 | -41.71772 | 2025-10-16 03:47:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df6138a1-91db-3478-bb12-0b0b2aa4115f | -4.38376 | -43.38594 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 709eb243-fd16-3ab3-9586-7234a567a750 | -11.43127 | -44.14518 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec6e5537-c145-382a-b13d-29e11b72eba6 | -5.46966 | -42.92915 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 76bf2dad-f4a9-3b15-8a37-11d5dcfc4ef0 | -6.21236 | -41.55265 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0e903d5f-ff58-38e6-8caa-87066b7858cd | -11.20945 | -43.99369 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1629db62-8c5f-34e9-8e33-a99366cc2e8a | -5.21397 | -37.36591 | 2025-10-16 03:47:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b395e23b-d4b9-3804-8633-12a047176b09 | -10.81124 | -43.94404 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d29afc2b-4768-3205-8c1d-fd68e73dd273 | -5.54049 | -41.32393 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 05913543-dec0-3a3a-a5c1-812ff6584831 | -5.51196 | -43.20266 | 2025-10-16 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c29c77e-11e4-3e74-ba95-2144af3dc7db | -5.50237 | -47.30468 | 2025-10-16 03:47:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 84d4fe73-f98e-3819-8bb6-77ec70caded2 | -6.43039 | -42.09656 | 2025-10-16 03:47:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d0370c0e-a331-3079-9d52-68462b5bb4a3 | -6.18083 | -42.59922 | 2025-10-16 03:47:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 72907514-cfca-3ca8-9281-0973f7b25fea | -5.96081 | -44.79991 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f1dcf68-3a2b-385f-a7bb-60505254a083 | -4.92241 | -45.89589 | 2025-10-16 03:47:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a2f695ba-9240-3ae6-8ead-868a9c3349c4 | -4.39056 | -43.45931 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3984e4dc-bf6d-3d29-8174-9bf21ffbfbb3 | -6.21178 | -41.55606 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d23ed8e6-4627-320d-96e0-593c991f2169 | -5.83872 | -42.34413 | 2025-10-16 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0ee0ddff-7468-377c-b2cd-d0b5e3e0f0c8 | -4.88492 | -46.70837 | 2025-10-16 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cb0a64a-0817-38dd-96ca-f14678cf159f | -4.4046 | -42.15148 | 2025-10-16 03:47:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8f86a009-1efd-3703-810b-8e7254ca1277 | -6.61719 | -42.22577 | 2025-10-16 03:47:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dcbef76d-84a2-3518-a2f0-343f7458c7b2 | -10.61559 | -42.31202 | 2025-10-16 03:47:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bd7a8272-d72e-3422-9751-66fafd014789 | -6.42747 | -41.88524 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 484d5f64-d9d9-30ba-9103-c94f64519009 | -5.85305 | -43.87686 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f374973b-5d1b-37d4-b96b-c522279b796b | -9.69352 | -44.51417 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 865d2ca8-6072-343a-9922-c2854ce3c64e | -10.03541 | -43.82964 | 2025-10-16 03:47:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a6e6221-f91f-3ee2-b62e-f37940074d93 | -6.03302 | -44.31836 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9677d1d6-670b-36d9-9543-0a256b418445 | -4.10809 | -48.0402 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README26.md)
