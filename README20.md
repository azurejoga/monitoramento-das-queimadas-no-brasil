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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f45a9fda-8022-3f23-a1a2-2ea5598923c4 | -4.94919 | -45.02871 | 2025-11-05 04:12:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6a928f3-9f0e-389c-8fca-3976a1edc421 | -3.48937 | -43.6283 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 88ad731a-8e74-3c27-8715-253d645487f0 | -4.86063 | -44.62206 | 2025-11-05 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3561e72c-6276-3515-a760-b0ba82e37ea1 | -3.78979 | -51.31389 | 2025-11-05 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc2e5a07-5479-3e9f-a4f7-6587c430ac35 | -3.80047 | -42.58706 | 2025-11-05 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11a8685e-72f6-3c80-8469-8571342ad11d | -4.45105 | -43.2201 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 0dd6a0ef-833e-33a8-99cb-a69fd511ec6b | -4.17912 | -48.58956 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cf8d398-5d3f-3226-b0d6-28d8e69ee8dd | -3.2391 | -52.92129 | 2025-11-05 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75024298-cdce-3899-bd07-1aa5f033843b | -2.68708 | -48.47025 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fd7ee05-6b55-3f2b-9e97-01992dd164a9 | -4.91666 | -46.71948 | 2025-11-05 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 199db316-28e6-37ae-b836-e1a77874791c | -2.65753 | -48.51349 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eeabd556-c0e7-3313-8cb3-c4d65890ab86 | -5.9225 | -41.29415 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3b9ff524-25bb-34a7-89fb-dfa9ff2cebf6 | -2.29327 | -48.50947 | 2025-11-05 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04866ced-68c7-3050-8cd9-bf1b458ebc00 | -2.89172 | -51.0147 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8d0b344-5a19-3d13-b65f-53ae27c8cc81 | -3.70713 | -45.8869 | 2025-11-05 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 569d8764-1afc-349c-af12-a3e44be376b4 | -5.92756 | -41.35059 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 090991a4-14a3-390d-88c9-10807a5e60ca | -6.09997 | -41.71869 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a50763f6-9702-336d-b702-de7c8561a4d1 | -2.48322 | -49.23473 | 2025-11-05 04:12:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fab628a-fa73-3373-aede-6e2a3eaeb697 | -5.47171 | -43.5779 | 2025-11-05 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da061ed0-75b8-3584-86a5-2c3f048a3c68 | -4.46983 | -43.23015 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 3d2063c6-0526-3a9f-b9a5-a9eb2145cb85 | -4.41762 | -48.94736 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 434bcffc-1e0e-3203-acea-812c374eca6c | -4.87543 | -43.26588 | 2025-11-05 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9650fc9b-7801-39f6-8c82-9c1d0071da54 | -3.85768 | -49.36559 | 2025-11-05 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a37cb80e-fec2-3614-8a40-8b969ab928f9 | -4.52376 | -40.35104 | 2025-11-05 04:12:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ea650db6-7080-3688-a335-21fff359c9e9 | -2.88126 | -49.59593 | 2025-11-05 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b35d7bcd-6c6f-3d94-85e2-4c75232953f8 | -3.80378 | -42.58758 | 2025-11-05 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3269b1af-32f8-3440-afd7-15fa3cbe16a2 | -5.00877 | -44.20011 | 2025-11-05 04:12:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c43557a0-2cb4-31be-b459-0580dd4e57ad | -2.87655 | -49.59515 | 2025-11-05 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 068630ae-1518-3344-9bd0-ee40a8d06d25 | -4.45768 | -43.22113 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a0d9d169-a9f1-3f5a-8b01-97a9d59480af | -5.42194 | -44.64525 | 2025-11-05 04:12:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d896385-78d3-3d85-ab0a-30ca3c1b9e89 | -5.45758 | -45.40047 | 2025-11-05 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f991acc8-3eb9-3f60-b235-a4b87c9ba62c | -6.66271 | -34.97589 | 2025-11-05 04:12:00 | NOAA-20 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 0f0c218a-97e7-3347-9da7-3c2adb23b09c | -3.48602 | -43.62778 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43b7ad61-cdde-35c9-803c-faa072785724 | -2.83815 | -49.83304 | 2025-11-05 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e97a4e14-3d6d-3b28-972b-006fbf51be5f | -4.94357 | -45.61819 | 2025-11-05 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fb55fbf-7a39-335c-a63f-929ab7766332 | -4.18276 | -48.59433 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 390ff674-8522-34e0-a934-15c4b9df6fc8 | -5.10697 | -46.21945 | 2025-11-05 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ebb66a7-a543-3a76-862c-ef69c6ca93b3 | -2.84293 | -49.41675 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 43663ecd-927b-381a-87a5-3f4c39219b5c | -5.77394 | -40.80703 | 2025-11-05 04:12:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 504328c5-1679-3026-ba94-6d3090b7d60c | -3.31024 | -53.83926 | 2025-11-05 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84528e55-3de4-3078-8bfe-68c523598efd | -5.92022 | -41.37543 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9077ab5c-e140-307a-9bd5-691caa4831b7 | -5.9253 | -41.36507 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e1b36255-b578-3665-90ce-81315a2b5010 | -3.48824 | -43.6354 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e519c201-a10d-33aa-a3be-7a03530e5268 | -2.39617 | -47.14707 | 2025-11-05 04:12:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df3949a2-6ed7-3932-b950-356670d5d373 | -4.50593 | -45.43743 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70024524-1e19-3f55-9c3f-febdee30951c | -4.252 | -48.64259 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6373ff89-e504-381c-9cd4-b54bdcb01aa3 | -2.87853 | -49.5929 | 2025-11-05 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b82d30cc-d7df-3d84-8ecb-abd916d98d7a | -4.28139 | -46.93465 | 2025-11-05 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64e8259d-c510-3e90-be7d-c95e2546cdbf | -4.60965 | -45.71006 | 2025-11-05 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c75c375-2a54-39d2-8620-7f9b512fca6d | -5.93323 | -41.29205 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| baa3337f-3e15-3296-943c-0cff0283a4cd | -5.0296 | -44.79347 | 2025-11-05 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89aa8412-ebd2-39b1-b511-9c968f1043a8 | -3.23282 | -43.44279 | 2025-11-05 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de3bf270-3a01-3a6c-a8c5-d85c63e7a4d1 | -4.82141 | -45.76739 | 2025-11-05 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7113511-a57b-3ea5-990c-6e4f6b99ee60 | -4.65793 | -44.52946 | 2025-11-05 04:12:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44a6f621-2c54-3ac4-bfd9-2b139bcd9d30 | -6.17866 | -41.63227 | 2025-11-05 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 60eb5e90-dca6-3b53-b5f4-e748ec8f1ee0 | -3.815 | -51.29203 | 2025-11-05 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94be82d9-6145-35bf-b3d5-74604265fbdb | -5.03304 | -43.6229 | 2025-11-05 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 252add0d-270d-3e3e-8963-261de007b1bb | -5.42976 | -44.66164 | 2025-11-05 04:12:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 58c277d0-dc9b-3505-b931-08b8133e0539 | -3.85692 | -49.37023 | 2025-11-05 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48a5407c-9bad-34b5-af97-58929ab57c43 | -3.23225 | -43.44631 | 2025-11-05 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f853448-8309-3739-859f-5090cb1c54dd | -4.10892 | -48.02113 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8989b45b-7d0f-3d06-8b4c-a16dc027825a | -4.4037 | -48.9495 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e268cab-ecc1-3df2-b86f-203abd44fb87 | -6.58171 | -35.25408 | 2025-11-05 04:12:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0767b2c9-7b85-35e7-bee5-ec0c490bfee7 | -4.18613 | -46.84028 | 2025-11-05 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bfe86b3-b55d-3fdf-a96e-02a7538bc34e | -5.14976 | -41.2174 | 2025-11-05 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 85696955-decc-3ba7-9ad1-87918b406ae8 | -4.28389 | -45.66174 | 2025-11-05 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9caba641-6fe0-3e12-9d6d-e5d215488816 | -5.37419 | -44.74388 | 2025-11-05 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 675746ae-a705-3711-b624-83060f78a786 | -3.24052 | -50.80011 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83453fcd-0ee4-3eea-ab95-20f8484a52e0 | -5.45694 | -45.4044 | 2025-11-05 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 4fd3395b-6720-3f6a-9369-bcc0cdc6f16f | -5.51259 | -41.15804 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 614fb40e-f2ad-3a31-b85b-1fd600e84d96 | -6.09648 | -41.70416 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0301189c-5969-3cbd-aa76-1f91d755deab | -4.46265 | -43.23257 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7bf2eeb-e0ce-3c54-9e2d-16ba608b207b | -3.81868 | -52.3631 | 2025-11-05 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1e914d2-86ce-36ac-baa6-2c919ed53d7f | -4.70652 | -45.6334 | 2025-11-05 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9d727e4-22d0-35f2-a5dc-08eaca59ad4e | -3.31644 | -53.84035 | 2025-11-05 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5bd572b-c8e8-3466-abcc-6a3b91245d66 | -4.04603 | -43.48098 | 2025-11-05 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74d85838-87a4-3f35-bdf8-66656e606010 | -3.48993 | -43.62477 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d1cc80d5-3b6a-37c5-a089-477492b75128 | -3.08614 | -48.67822 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86d171cc-2803-36a3-b827-4c66fe44542e | -4.41691 | -48.95163 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e7548a17-c24e-35cb-8c49-9ad74be715ac | -6.1529 | -41.64303 | 2025-11-05 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 09a15879-d42d-37cc-9571-d0041d457e27 | -3.48757 | -50.4642 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8686762b-6266-30bd-beb1-1d2100274fb0 | -4.67539 | -45.80528 | 2025-11-05 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6d84bb0-faec-37d5-b50e-443ec44f308e | -3.2384 | -52.92545 | 2025-11-05 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 654defc8-2600-3352-a97e-137c18b79739 | -5.92755 | -41.37283 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1c6a009b-373a-33b4-b637-0741c66aeed8 | -3.6565 | -44.79831 | 2025-11-05 04:12:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 64a55aed-a722-3804-acf7-f27feb586e99 | -3.48323 | -43.62372 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9391ced2-d896-3776-930b-0379036047fa | -3.71009 | -45.89178 | 2025-11-05 04:12:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d2430266-f3e2-3f81-be88-d01885e3ecd6 | -5.10994 | -46.2243 | 2025-11-05 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88386b3b-0927-3189-ada2-4a324f97ca7c | -3.13047 | -44.47636 | 2025-11-05 04:12:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4f0dde1-a0cd-39c6-a841-43e6fbaf2ddc | -4.97256 | -42.86748 | 2025-11-05 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bae5ff15-34fb-3ccd-8d5c-5b45722e6dc4 | -4.61835 | -46.59777 | 2025-11-05 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 986aedb7-321d-3146-839a-f7c02768d5e6 | -4.45649 | -46.63924 | 2025-11-05 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 22466b8a-1642-3397-b088-f2dc8a9a2c16 | -3.82341 | -48.66679 | 2025-11-05 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b61ec47-bdae-3a58-b868-ef3bbfb695c0 | -3.77039 | -47.96084 | 2025-11-05 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6676727d-f55e-302e-8f3d-e5ab5d407283 | -4.766 | -42.64826 | 2025-11-05 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1daa33d5-8eee-3179-a365-2eebf9e1c18b | -3.77028 | -51.71742 | 2025-11-05 04:12:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eabc8747-388e-3ff9-be82-979af00ae695 | -2.47796 | -55.73194 | 2025-11-05 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d36a3018-1b8c-39e0-a92d-3becc48c7be4 | -5.92698 | -41.37645 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f6633fa8-a1b1-39e4-8107-9f69ead6d0ca | -3.33558 | -44.35463 | 2025-11-05 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e11f96d5-0e77-3d8b-9504-5cd5c951e13c | -4.76161 | -42.65462 | 2025-11-05 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |


[Clique aqui para ver as próximas entradas](README21.md)
