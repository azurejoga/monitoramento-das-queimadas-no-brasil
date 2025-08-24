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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c704defe-e4ed-35b0-b7ba-d45dfaaf61bd | -6.09582 | -44.69505 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67551983-2c0a-3f85-a8ef-6885db5c3915 | -6.08858 | -44.69389 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51844185-8d7c-3715-8c4f-b728e3c1c7cd | -3.24905 | -46.90337 | 2025-08-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1118dae-6272-3cad-85b5-021714519825 | -4.58554 | -48.03661 | 2025-08-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78928d46-615d-38a7-bd88-1b9506041562 | -6.21093 | -42.9985 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1debf7f-5d44-3b35-8364-93b28422bea0 | -2.93214 | -53.69888 | 2025-08-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 806082c5-e7e0-353b-ad5d-edbee3e81214 | -6.09284 | -44.69025 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e57b9566-480f-3fb1-9420-0f6fc84b38e4 | -6.72393 | -42.99374 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b8b11823-9c37-363a-8bb2-bd70dad7ed5f | -6.12505 | -44.37912 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31c23cce-a12c-37fa-a9cc-5a503bb59a36 | -2.9284 | -53.69381 | 2025-08-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5cb18834-2097-39d9-9c7b-94e36ef551dd | -5.58493 | -45.80789 | 2025-08-24 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a29f6dd-699f-3146-83c9-cc1c8d7459b4 | -6.02299 | -42.80505 | 2025-08-24 04:32:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b512f965-4af3-3e05-b630-0f1c6d726694 | -4.82409 | -47.31622 | 2025-08-24 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60996576-20a7-3cca-8695-7dd9507f47d4 | -6.70677 | -42.9692 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 68090774-8840-3cf5-978c-41e0bf37e2bf | -6.12572 | -44.37467 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c6eb616-f6cb-38bf-bab0-85f8958264ef | -6.67313 | -44.41719 | 2025-08-24 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 456b0964-fa09-3932-ae99-04a36fca514b | -2.95255 | -48.05962 | 2025-08-24 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cc6c706-9cd2-3d81-aa0f-cb26b94e3ab9 | -3.76411 | -49.61916 | 2025-08-24 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab56daa9-6d86-35f6-bb6a-4f3cdf09aa71 | -4.30043 | -48.07713 | 2025-08-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cadecde-38ba-3dbe-a0c4-06b35249b3ef | -6.47204 | -43.45744 | 2025-08-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa15425f-ae26-3490-becd-baf4ce734ddd | -4.48374 | -47.66805 | 2025-08-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd820263-48ca-3ddf-9661-09b57f82e3b8 | -5.66173 | -45.14217 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 80f7b0c0-aa96-3751-9b17-1a87c90572e2 | -6.10307 | -44.69615 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e4c5080-c2d7-36c6-b9ee-392704e18dda | -4.48705 | -47.66857 | 2025-08-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| bf00454a-de96-35a6-93ba-5691eb81f5ec | -6.22958 | -44.78142 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ea8d902-a210-33eb-96d1-0b919d262ef5 | -6.7233 | -43.19521 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 185731e1-03c4-39e3-acf2-5d54a24d0b08 | -6.50399 | -43.103 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da979e16-9ea9-3067-9a48-92cd1cc97f49 | -6.05786 | -44.0023 | 2025-08-24 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 59cc819b-7343-3e1b-91b7-a9cf70033239 | -6.1274 | -44.38851 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dede455-630e-3e37-95ea-823b757bfef5 | -6.43294 | -44.54544 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 985b0111-2da6-3312-8ad8-b4fcc270533c | -6.22659 | -44.77668 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5b1fc29-5a7f-3da7-a447-b77567663afb | -6.13041 | -44.39351 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 794c2df5-f27e-3d5a-8769-3b33a51da9e1 | -6.84596 | -44.40769 | 2025-08-24 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e13edbd-09d3-32a5-8c65-151f9cb4c7b1 | -4.93452 | -43.16713 | 2025-08-24 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 30fe5f15-2d34-3eea-92ef-c24f80d8857b | -5.4169 | -44.98926 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| badd34d5-5594-3f58-8b93-f86a53c2b086 | -3.59697 | -47.52813 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a7acf95f-9c44-3814-bae7-934400422648 | -3.54613 | -41.62091 | 2025-08-24 04:32:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ffe545b0-8a7f-362b-af0d-b01e072f043c | -4.48819 | -47.68284 | 2025-08-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9901b85b-1f34-3cdd-ba54-0ddeeaf6edbd | -6.76652 | -44.31539 | 2025-08-24 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e941deb-8407-3726-83ad-4b1a7bd866fc | -2.52359 | -47.38763 | 2025-08-24 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a617d6d-d9fa-3c46-99f5-bcde94dd6172 | -4.28186 | -48.64943 | 2025-08-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cae58290-6934-3100-8ec3-6d2bd01b3e95 | -5.74839 | -40.44696 | 2025-08-24 04:32:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5c4074cd-6e1f-3387-a308-9931ac44b645 | -3.79401 | -47.57357 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c74e21c3-c0da-3a9b-9b29-cee131486211 | -5.78706 | -45.10402 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9dc5078-8af6-32b0-914d-e1f82bc24ff7 | -5.41001 | -44.98873 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ba58ff4d-0005-3fde-95c8-b898768829cc | -2.2568 | -47.85439 | 2025-08-24 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7b729cc-f24f-335c-8a26-e111349f441a | -4.64157 | -41.41932 | 2025-08-24 04:32:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4f2f3a27-2192-3292-b083-dbca0492e727 | -3.36655 | -49.16077 | 2025-08-24 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93c0ec66-c3a8-3d56-976b-13d98ae98e02 | -6.91796 | -43.78392 | 2025-08-24 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e540e60-2b3e-3524-afd0-32d096065b81 | -6.21688 | -48.45889 | 2025-08-24 04:32:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd00c653-1b62-3e03-88be-c26902c0f64f | -6.189 | -45.43629 | 2025-08-24 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a5c16e38-7bb8-3d77-840b-34024b9515ac | -6.82711 | -42.82434 | 2025-08-24 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 608e9e0c-ee64-3ea9-bac2-3adb11cd23ed | -3.38652 | -47.6152 | 2025-08-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec94fcc6-eb04-30ed-8811-93293d68d2b8 | -5.7002 | -49.14546 | 2025-08-24 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed9e3da8-9127-3fdd-9ca8-64e6e9a7cbdd | -3.55036 | -41.62157 | 2025-08-24 04:32:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0f33154a-9ded-3378-a371-9b0dae02fe66 | -3.40201 | -46.90576 | 2025-08-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32b1180f-285a-34df-983c-654ef890ad72 | -3.7365 | -48.93189 | 2025-08-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3204347f-7b70-3356-82c1-567cb7cab133 | -6.72501 | -43.12776 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f40bed4-0f13-3e5a-9900-4283c0ef65ae | -5.66345 | -45.15462 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1757bfb5-ba76-31a6-b378-52c1dbfa3d40 | -2.93283 | -53.69452 | 2025-08-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c7b982ce-0353-35cd-a1d8-e07cc7dd2ad4 | -4.9612 | -55.82339 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| a8464cde-5910-3272-8cc7-3af25ecd6853 | -6.1931 | -45.4329 | 2025-08-24 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 35a32f21-7456-3239-9aae-3d5383a7546f | -6.67008 | -44.41224 | 2025-08-24 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8db9bca-5f3b-3c29-a089-d283600b4f09 | -6.83722 | -44.41545 | 2025-08-24 04:32:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68ccd2b7-2e7c-39fc-ad97-480cc3e6876e | -2.63013 | -58.10963 | 2025-08-24 04:32:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46e9d562-79fe-3b6d-b11c-19aff602810c | -6.71744 | -43.86176 | 2025-08-24 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f27964d0-3c44-3704-9bf9-93c4f7ac4cb7 | -5.87775 | -42.91711 | 2025-08-24 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1219a80a-91cb-35c3-8bc8-fd2689551715 | -6.71931 | -43.1946 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7e6880a1-0f0c-36f5-a3cf-51df835adead | -2.63386 | -58.10941 | 2025-08-24 04:32:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d00fe834-9d77-3223-a2af-7943ec020fa9 | -4.31041 | -48.09994 | 2025-08-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8bbc4c22-f072-31eb-a5c7-08497f9b2e28 | -5.64825 | -51.84409 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70ea467a-5dc3-3d1f-ae54-28523f2c6b3b | -6.67379 | -44.41283 | 2025-08-24 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05b8de12-971a-353b-949f-d95d80f5b29c | -4.2457 | -47.27464 | 2025-08-24 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8e90acf-a354-33b6-aabd-eb5b3df42c7b | -6.25906 | -42.6717 | 2025-08-24 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0c99ee64-a734-3948-a0d1-d25a0ea67e6c | -5.74223 | -45.35152 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b839ba1c-54f5-3393-b63b-b252b8dbaf07 | -6.205 | -42.98301 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c5ceae0-9602-383c-981b-009598922740 | -4.96749 | -55.82209 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc6c8552-a12d-3c93-a5f4-65174dcec1f6 | -3.43722 | -49.04451 | 2025-08-24 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| be5a125a-1558-3037-86c4-6d82c53c7c64 | -6.26486 | -44.33839 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8687c96-e07c-338a-9898-3c409d1c7f26 | -7.05867 | -41.90814 | 2025-08-24 04:32:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8c141386-09a4-31cc-9c5a-4d439ead4817 | -4.96648 | -55.82788 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6e98d27-7352-34ed-a505-df957df848cf | -6.11161 | -44.36811 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3822bb96-d25e-3afb-9d39-af8f92e6f5cb | -4.31427 | -48.097 | 2025-08-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef9efde5-2544-3884-917e-8fe4916cadd9 | -6.18669 | -45.42794 | 2025-08-24 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2fbc4136-3c35-3177-a4bc-35e596acaf3f | -3.76745 | -49.35546 | 2025-08-24 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cbdd1f3-f943-39a7-ba79-dd428b7b1327 | -4.22508 | -47.21154 | 2025-08-24 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9fa7111-5d1a-38d9-9420-eaad7f43a712 | -6.11973 | -44.41438 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77f6a936-265a-3969-a867-6cdbdb689e76 | -6.1902 | -45.42848 | 2025-08-24 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a1516b38-f720-352a-a20f-889b7068d2c9 | -6.11907 | -44.41873 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b267f5ab-c583-3e29-b116-aa0ac725a9b4 | -5.37375 | -41.2148 | 2025-08-24 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2fd2e41a-152a-3c87-8cf1-f849182299a9 | -5.68058 | -45.13697 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd320773-bae6-3705-89ec-7224303b4877 | -4.4799 | -47.67098 | 2025-08-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56c7a35c-7bec-3f23-8c35-6e2a62fddc97 | -6.11227 | -44.3637 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8287f6e2-23f7-3332-81ab-dc1ce19bbf22 | -6.58689 | -44.56558 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3c53c01-a954-3856-abea-a751c4495557 | -6.31014 | -43.76437 | 2025-08-24 04:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6bef6bb-e8ec-3e1b-ab35-6a7cde7db732 | -3.79418 | -41.005 | 2025-08-24 04:32:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4f102517-6c69-323f-a9ad-6d957f423201 | -6.01894 | -42.80444 | 2025-08-24 04:32:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| da9f83ad-5ef3-3456-a57c-b21776acc974 | -6.0862 | -44.38674 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80ec6536-5a83-33c5-9f0d-4b859b77dfe8 | -6.12807 | -44.38411 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98409ba2-d761-34b5-a548-995e93adc6b9 | -6.19251 | -45.43679 | 2025-08-24 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README35.md)
