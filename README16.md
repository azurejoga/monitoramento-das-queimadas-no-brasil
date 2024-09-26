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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1052edb3-e3a6-31b3-b49d-6cf0cb533e43 | -14.915 | -58.0055 | 2024-09-26 00:46:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 8e90aa05-6db8-3d3b-a8f4-2b3262859388 | -14.9153 | -57.9854 | 2024-09-26 00:46:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 172.8 |
| c02dc88d-c3bf-368e-a0d0-e4f79c8a9cf4 | -14.9156 | -57.9653 | 2024-09-26 00:46:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e3bc6001-dee7-3bb6-b73f-b4d6f1f19ca0 | -15.3175 | -58.1872 | 2024-09-26 00:46:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e074714b-58b1-3e3f-a6e4-fb5b883cedda | -15.2981 | -58.1891 | 2024-09-26 00:46:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 4143f5f4-bc32-393b-9d93-f5d512df54b5 | -19.929 | -43.7959 | 2024-09-26 00:46:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| 6f2820a3-b3cc-3133-b92e-0799a171cba5 | -19.9298 | -43.7711 | 2024-09-26 00:46:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.7 |
| 46a9b7a9-07fe-3eef-8bd0-7692cf69c536 | -20.399 | -41.886 | 2024-09-26 00:46:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.6 |
| 02065963-23e1-390c-83c7-871bef5c7deb | -20.3999 | -41.8602 | 2024-09-26 00:46:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.2 |
| d828fac1-5ab5-3a41-939c-e37cb764b830 | -20.4197 | -41.8798 | 2024-09-26 00:46:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 114.0 |
| 0223cc36-3586-313d-9d0b-6af85071a2c4 | -20.4206 | -41.8541 | 2024-09-26 00:46:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.9 |
| c829c749-b553-3e16-84fd-8a30dee501b6 | -20.5876 | -51.5026 | 2024-09-26 00:47:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.9 |
| dc9d71a8-218d-3412-974a-81664e1dee12 | -20.5881 | -51.4802 | 2024-09-26 00:47:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 172.3 |
| e08e5b01-9f64-30dc-be3d-70b39fcda02f | -20.608 | -51.4986 | 2024-09-26 00:47:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.5 |
| 59b8300e-7966-351d-8a74-12c9fae00754 | -20.6086 | -51.4762 | 2024-09-26 00:47:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 157.0 |
| 9b4951b1-0b10-3701-8c84-2e2144ac87db | -3.01412 | -52.18994 | 2024-09-26 00:48:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 8b55de75-58e0-38ad-91e3-5259c7defe29 | -2.87667 | -51.66388 | 2024-09-26 00:48:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1c52b581-b9f0-3a82-ac24-2bac3d2f646f | -2.65766 | -54.62781 | 2024-09-26 00:48:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| cb688ae8-fdd2-391d-ab4d-88f630cf430e | -2.6534 | -54.62202 | 2024-09-26 00:48:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 2476e996-ba86-3377-868d-6aecb93df77a | -2.56097 | -54.61074 | 2024-09-26 00:48:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c66f794d-9cc7-3fdd-a5a2-64ffdd9b6f0a | -2.54949 | -54.61802 | 2024-09-26 00:48:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d7c5bd82-b677-3dfc-bef3-6aa0b8caef97 | -2.39144 | -51.29511 | 2024-09-26 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 770d02ca-f36b-3e95-b34a-a74985dfbd93 | -2.38917 | -51.27889 | 2024-09-26 00:48:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 9f1edc67-eba5-3c17-b026-c5e15e34a8a2 | -1.98252 | -45.86269 | 2024-09-26 00:48:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9f420da4-bb16-3c39-a94f-8c0641712256 | -1.9813 | -45.8539 | 2024-09-26 00:48:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d3285a37-1c19-3f6d-a0b6-e77033f6f45f | -1.94301 | -47.90329 | 2024-09-26 00:48:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a2450271-b5ba-3816-8e67-ddb9c92467cf | -1.9048 | -47.88543 | 2024-09-26 00:48:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5eda1679-7f96-376d-a199-85edf1b75eb5 | -1.17329 | -46.8639 | 2024-09-26 00:48:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| ca0bf6b7-6c22-3ed1-8182-6c722a9a4027 | -1.12423 | -46.9129 | 2024-09-26 00:48:00 | TERRA_M-M | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8fbb13e6-b1f7-3d8b-9890-b5d59973040b | -1.11359 | -52.17372 | 2024-09-26 00:48:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 55e1a87d-80cd-39e6-acc2-a695a52b8743 | -1.05591 | -53.36621 | 2024-09-26 00:48:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 64f0072e-420b-3354-84b3-b45d65e5366c | -1.05287 | -53.34401 | 2024-09-26 00:48:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 781976aa-1276-322a-a881-f173f45c2909 | -1.04855 | -53.37369 | 2024-09-26 00:48:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 41bba816-1a28-3406-ba38-0ed03b58b683 | -1.04534 | -53.35134 | 2024-09-26 00:48:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4e7a0bb8-16c8-37df-9269-baaa2e0348b2 | -1.0423 | -53.36824 | 2024-09-26 00:48:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| a01809c9-b986-3be6-8932-4528362603ef | -22.5861 | -43.958099 | 2024-09-26 00:52:12 | METOP-B | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98f961c4-c227-32cc-b838-56eef2dd6afe | -22.589199 | -43.9702 | 2024-09-26 00:52:12 | METOP-B | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c64e782-6706-3489-882e-9aa772b28a80 | -23.3452 | -46.982399 | 2024-09-26 00:52:12 | METOP-B | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c4cc4bc-0bec-3234-9539-16a5f2fb50ab | -23.3472 | -46.990799 | 2024-09-26 00:52:12 | METOP-B | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7eec071-4cba-3f3c-bd9f-bd840f7f9ee1 | -23.623899 | -50.875999 | 2024-09-26 00:52:21 | METOP-B | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 455ede0c-6e1a-34c2-92fc-85f5010da93a | -22.8748 | -47.812302 | 2024-09-26 00:52:22 | METOP-B | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eb6a3417-e1a7-3ebc-9327-aaf2b5f7eba0 | -22.8766 | -47.820301 | 2024-09-26 00:52:22 | METOP-B | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5703689e-8cc7-3c1b-8ff4-d2c63049a6bc | -22.8785 | -47.828201 | 2024-09-26 00:52:22 | METOP-B | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0eed005-81d6-3e6d-99a4-120b2defa66c | -22.8405 | -47.617599 | 2024-09-26 00:52:22 | METOP-B | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1db5d116-c601-3f0b-84ec-06db76b9d985 | -22.8423 | -47.625599 | 2024-09-26 00:52:22 | METOP-B | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f7afb4bd-83b2-3f50-afa6-0520763e72af | -23.162399 | -49.9995 | 2024-09-26 00:52:25 | METOP-B | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b52f780-46a8-3ea7-9f8c-a49876386f8d | -23.164 | -50.006901 | 2024-09-26 00:52:25 | METOP-B | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c3166d0-bb55-33d0-9b97-11f84d39e601 | -23.150299 | -49.798801 | 2024-09-26 00:52:25 | METOP-B | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9bffd8ff-7be4-371f-8f21-1eefe9e79e4f | -23.102301 | -50.296799 | 2024-09-26 00:52:27 | METOP-B | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb53deb8-f9a3-3303-9d8b-1564ebd294d0 | -23.103901 | -50.304298 | 2024-09-26 00:52:27 | METOP-B | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb729d1c-3e4f-3979-b049-f98c456da96e | -23.105499 | -50.311798 | 2024-09-26 00:52:27 | METOP-B | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d8b9216-9a51-36f9-9ff5-e322469d6eeb | -22.3682 | -47.632 | 2024-09-26 00:52:30 | METOP-B | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0ab6063b-316b-3d00-b028-19d3a7653051 | -22.353399 | -47.747299 | 2024-09-26 00:52:30 | METOP-B | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 32126256-d993-3a27-8575-2151e9079dcc | -22.3552 | -47.755299 | 2024-09-26 00:52:30 | METOP-B | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ae4495d1-dec1-316b-b0bf-36a07ba04b71 | -22.357 | -47.763302 | 2024-09-26 00:52:30 | METOP-B | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a0091470-c194-3ac9-840c-972083e5c108 | -22.3589 | -47.771301 | 2024-09-26 00:52:30 | METOP-B | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3a8d4b2c-7ccd-3252-b606-8dd68829d893 | -22.3417 | -47.741798 | 2024-09-26 00:52:31 | METOP-B | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 989695e9-cae5-37b5-8d4d-1ed141e8557d | -22.343599 | -47.749901 | 2024-09-26 00:52:31 | METOP-B | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 913bb644-cc38-3b09-8858-de29bf6f237d | -22.3454 | -47.7579 | 2024-09-26 00:52:31 | METOP-B | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 64658131-ef10-3470-a797-a85dcdf4f0a8 | -22.215099 | -47.5518 | 2024-09-26 00:52:32 | METOP-B | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 794e9c71-b32f-3c99-97bc-5300d4d95e59 | -22.216999 | -47.560001 | 2024-09-26 00:52:32 | METOP-B | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4c052162-3bc4-30c9-b9c2-251faef506b2 | -22.218901 | -47.568199 | 2024-09-26 00:52:32 | METOP-B | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 207f8461-2ab3-38de-9b69-55af8b2978df | -22.2054 | -47.554401 | 2024-09-26 00:52:32 | METOP-B | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9331543a-72d2-32e2-8b16-d823446c7feb | -22.2073 | -47.562599 | 2024-09-26 00:52:32 | METOP-B | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 382a80d9-9e48-3e89-a70d-904669f9dae9 | -20.2885 | -41.2248 | 2024-09-26 00:52:37 | METOP-B | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ee2dd654-e01c-3594-9fff-c5a2d3a5efb7 | -20.416901 | -41.847301 | 2024-09-26 00:52:38 | METOP-B | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f7675ef-0f81-3652-ba33-ee0c240e7c3d | -20.4217 | -41.864899 | 2024-09-26 00:52:38 | METOP-B | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 491e854c-554d-3441-a298-ab1504e7ff3b | -20.407301 | -41.850201 | 2024-09-26 00:52:38 | METOP-B | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49131d7a-cc76-3efa-8a98-18241f12f9b0 | -20.4121 | -41.867802 | 2024-09-26 00:52:38 | METOP-B | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 971ed1eb-be84-3aa3-a61b-495fef6d2b85 | -20.397699 | -41.853199 | 2024-09-26 00:52:38 | METOP-B | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49226ea6-acc0-3aa3-9c7a-30b732c5ed47 | -20.402399 | -41.8708 | 2024-09-26 00:52:38 | METOP-B | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd8dcd77-45f2-323d-82f2-a9356230de61 | -20.273899 | -41.436901 | 2024-09-26 00:52:38 | METOP-B | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4587a890-e6fc-39e2-89b5-e0951bf64852 | -20.383301 | -41.838402 | 2024-09-26 00:52:38 | METOP-B | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7114e38d-911c-3093-b7fd-12a8bd78f8bb | -20.3881 | -41.856098 | 2024-09-26 00:52:38 | METOP-B | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| efb06d74-8ca3-3054-9c11-99f4b4439a21 | -20.392799 | -41.873699 | 2024-09-26 00:52:38 | METOP-B | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b4e505c-da32-3939-ab7f-6b3caf0d02ef | -21.9494 | -48.559299 | 2024-09-26 00:52:40 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 416612ed-6c11-39b5-9b68-305f84b212e4 | -21.2043 | -45.745098 | 2024-09-26 00:52:41 | METOP-B | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 91e551be-abe4-3f13-84b4-79136c62873f | -21.2068 | -45.7551 | 2024-09-26 00:52:41 | METOP-B | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 67572db9-e152-3953-ab45-633546532ce5 | -20.517 | -43.9188 | 2024-09-26 00:52:45 | METOP-B | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 215eaaa5-3eeb-335f-b4bb-770b6d5f1ecf | -20.149401 | -43.502701 | 2024-09-26 00:52:49 | METOP-B | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f03703fc-4d46-35e9-9482-d38b69cbc121 | -20.1567 | -43.530701 | 2024-09-26 00:52:49 | METOP-B | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 907a25b4-0a4b-3cfa-a2d9-90660bad244f | -20.821301 | -47.2117 | 2024-09-26 00:52:53 | METOP-B | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53c9ae89-2f03-3cc5-a10f-51093efe6075 | -20.8234 | -47.220299 | 2024-09-26 00:52:53 | METOP-B | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7b963981-29bd-3f58-93ec-d1cf9fbdeb6b | -19.9256 | -43.761398 | 2024-09-26 00:52:54 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 15ad67e3-2e54-359d-8059-cb1fc42ca786 | -19.9291 | -43.775002 | 2024-09-26 00:52:54 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a734e1f8-c796-3c2d-a69b-e581f8f3a9e2 | -19.9326 | -43.788601 | 2024-09-26 00:52:54 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbc8e8f6-b8b8-351e-bc6f-f66838a1e68e | -19.915899 | -43.764301 | 2024-09-26 00:52:54 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8982d33f-4f63-3b6e-b60a-1c207e568f8d | -19.919399 | -43.777901 | 2024-09-26 00:52:54 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 318c7bd1-810c-3d1d-b267-f7c8836327fa | -19.922899 | -43.7915 | 2024-09-26 00:52:54 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa6f1e4f-fbee-3ee7-935a-c380f1dfb79f | -19.9097 | -43.780701 | 2024-09-26 00:52:54 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 36c27b68-5b29-386c-be7f-99b79c74b229 | -19.610001 | -42.795601 | 2024-09-26 00:52:55 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03230571-b22b-31af-83ef-39128c40123c | -19.605801 | -42.7798 | 2024-09-26 00:52:55 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 54e6a64a-fb7a-39b7-9dd3-3e2d9ad450bd | -20.999001 | -49.059898 | 2024-09-26 00:52:57 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 46f76985-64c5-3c17-b364-0c7416ba306e | -21.0007 | -49.067402 | 2024-09-26 00:52:57 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 59088e79-57c7-3870-bf8e-3c774bb06f1e | -21.002399 | -49.074902 | 2024-09-26 00:52:57 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e9687c1d-dd12-3989-a3e1-da4c868bbf78 | -19.948299 | -44.949501 | 2024-09-26 00:52:58 | METOP-B | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fc32d512-5c04-3d59-a7f7-967e00f7a3f2 | -19.9512 | -44.961102 | 2024-09-26 00:52:58 | METOP-B | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| abb901cd-6c8d-3756-94d8-6b0763f6a23f | -21.2747 | -50.982899 | 2024-09-26 00:52:59 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e773a8b9-7917-368a-b2eb-b1aba4f2ecad | -21.2763 | -50.990299 | 2024-09-26 00:52:59 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 535e1d80-8b26-3da0-9f48-3ba7fcd9338c | -21.2778 | -50.9977 | 2024-09-26 00:52:59 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README17.md)
