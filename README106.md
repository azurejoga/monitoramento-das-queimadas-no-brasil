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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d168bb7-f293-3665-adb6-d738bca73c7b | -3.58312 | -54.66904 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| df4e7a47-9b6e-30df-bb90-9ee02f4b2c69 | -3.29116 | -54.05085 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ff41de4-a857-3c04-8a89-1c276a4eb250 | -4.56209 | -54.95546 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13914e67-18c7-3483-8488-95fe74568b6c | -6.25928 | -55.99575 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2f9e32c-3a0d-366a-b9b1-bedd4cb599ad | -3.2807 | -54.02274 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f21a6557-b593-301b-bdf6-de83e3a26180 | -3.52255 | -54.65929 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df0c5e1c-5301-3f33-940f-417633cbb1da | -4.27248 | -55.71518 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a931e4e-f779-3829-b6c9-b37944d9917b | -3.1256 | -53.70577 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a376fea-1e1d-3d13-8104-baf7827b4db3 | -3.11875 | -54.16953 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 5bcf8a76-e3a4-340e-a22c-e1358945b848 | -3.85253 | -55.98394 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c36fde8-ac6c-3dc9-958b-1f739b246a40 | -3.30861 | -54.03594 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bf67ecf2-723f-3f5a-a6a4-75fdca41e59d | -3.09841 | -53.72835 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fdd497f-3e2f-3ced-bad6-c068bffccbb6 | -3.79357 | -52.32504 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16401e39-e545-3bf9-9382-5f4bc1ff7ac1 | -6.11812 | -55.70454 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6707f82c-9fc7-3a73-b01c-3729d36794ff | -3.52494 | -59.35436 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16c4dd0e-7cd6-339c-941f-8cadd7e92e41 | -3.62934 | -55.50957 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb43fc34-710b-367a-83cd-db4d70ba7d98 | -6.30788 | -43.34215 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 50f94c4f-1c9b-3bf3-99a8-82c1b97c079d | -3.85314 | -55.98028 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c13ad5e-7e5a-366f-8cf9-62f7f670ddb6 | -3.56826 | -54.2212 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba000b83-3a61-3b6f-96f0-629509fb546e | -3.50298 | -59.2856 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31d8d786-d02e-33b3-8f22-77d93db4b8ce | -2.89289 | -54.07915 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02550c63-187a-3bcc-b754-58adaad69364 | -3.10321 | -53.77525 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3e02ef1e-f616-3b6b-a101-a04d5656b92c | -4.09442 | -52.0623 | 2026-10-08 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cc6d39a-c282-31ff-a90c-75ce030e1b44 | -3.06767 | -59.27693 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dae17ffb-26df-3120-a79e-02500c1e7396 | -3.2823 | -54.03765 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7f6a471-8491-3f0c-8ac5-5c6a0c9e2e8a | -3.04889 | -53.92433 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02545ce0-0757-3c1b-be93-6ab4fe2ec209 | -3.36647 | -50.47618 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f6d5b52-3a66-307d-87c4-23caf9c78ee4 | -3.18452 | -58.65099 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38a9a313-2585-3090-b2a5-3f7a6480bb86 | -3.07426 | -53.95327 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 49abe502-1ac5-3139-aa6f-655863ff52a9 | -3.06479 | -54.17458 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6a0ca52-8b96-38a8-aa87-38a7becfc0eb | -2.86396 | -54.16502 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5e36ebf-7a8c-3206-87f4-99068f042f7a | -7.90099 | -54.7216 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ec309a1-1355-38a8-81c2-6aaff81ce11d | -3.08559 | -54.28234 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a64ed35d-1d86-343a-93e7-f1ae74d1d077 | -4.71858 | -47.44587 | 2026-10-08 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f4e2513-6a9d-3eaf-8cc4-bc5c330f4ea7 | -3.03188 | -54.10355 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c504bad5-bed7-3fa5-85a9-55abae05fd9f | -3.15635 | -54.09907 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 918666c8-48f4-3749-a2f3-856d123c31d4 | -4.76473 | -55.72777 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4184e52-083b-3c30-b989-1dc593ce1242 | -3.08661 | -53.94651 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3941add-2b80-35fe-8182-b0d8e160e61b | -3.31089 | -54.04511 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| db0ff30c-d299-302d-9e08-9ef81e6fbbd4 | -2.93335 | -54.17383 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38767f0c-04fa-3655-bbfc-9ad5ab0c89f6 | -6.04315 | -53.48351 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5646282f-1e73-3271-ade9-01f066ea0cad | -6.16141 | -52.6559 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2588cf1a-5bba-38e4-aabe-5bbdeadd7323 | -9.62119 | -47.77574 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55fa6cf8-7a35-356c-8525-5cccc8dba72c | -3.54073 | -54.66694 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d358603-0718-3a0d-86a8-f786bc0b86a7 | -3.06448 | -54.24728 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 680cde0b-265f-30b9-a41e-178be8e5a1af | -3.43088 | -58.59737 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 17261124-ce32-3fe1-aa7b-9d74c82da434 | -3.71716 | -59.33769 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6211ce6d-78a2-3632-9107-b0eaa7c612cf | -3.77301 | -59.25806 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f5b5f04-8e08-3f76-a8ee-05a0bb86f7c3 | -3.05342 | -54.26857 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7157365c-0656-3299-9c5a-32dee3e926eb | -5.49431 | -42.85229 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 854c3272-28c8-36ba-a909-adbea9b5c889 | -3.47908 | -50.08286 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d77c7f61-1a65-32a6-8a27-ce61d444c730 | -5.56151 | -51.73664 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4455d4ac-dae7-3860-94e2-b811ce41f55e | -3.56955 | -59.47205 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69b11815-172c-330b-9382-42e5b1c9b806 | -3.0185 | -54.09246 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ed34c554-804b-3f39-99c7-5da6af3a2778 | -3.87121 | -55.99826 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4c58cf8-f25b-3d92-930a-149d72b27d94 | -3.07296 | -54.28965 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bbfb66c5-a53d-37fb-aeff-18f0d5351859 | -8.17922 | -54.72594 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b2f31fd-279c-3693-9a23-f282e05687d6 | -2.84594 | -57.47739 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f074eeb7-7317-3275-9ae3-0980279a6ca4 | -2.97822 | -54.13128 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f74f55e3-c85e-3e5d-ace7-cfb62dca6d27 | -2.9858 | -54.06056 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 45a494a4-8c3a-3f15-aa40-69c0b3025c0b | -3.53316 | -54.66573 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70a38dce-192f-3088-bc57-6d3158725802 | -5.70315 | -53.47789 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3a310c84-fc86-3186-9980-639f34952013 | -3.99807 | -56.25238 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f42ddb2-3792-3bd7-9365-68595a09f1f1 | -3.28268 | -54.01125 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b3b6e7d-77fd-3614-9412-c42c86386cbf | -2.88589 | -54.12301 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f207f29-77c1-3280-a3fc-66b4f2b90a15 | -3.85147 | -50.41903 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f537d94-379c-3258-983f-195b3358492c | -3.16646 | -58.63639 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03b162c5-9390-3a5a-95fb-c016d4a4aa38 | -5.04484 | -49.76548 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3448996-c399-3873-b1dc-d1e0ae3a407f | -10.7352 | -52.03216 | 2026-10-08 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8da708ed-d3b6-37c2-bab4-deded4e8bae1 | -3.30499 | -53.87363 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd0ca0d3-f2be-3180-b788-563f2ff472cd | -3.26188 | -54.66236 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 23aeb529-72f3-37a1-b244-c5af1be34acb | -3.27084 | -51.06618 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bef870f-e9ff-3f4f-a509-b2a7e87911fe | -3.52708 | -54.65529 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60c5f0ac-87a8-32c7-adfb-d6c6060abffb | -2.90207 | -56.66874 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc8a5069-7d29-31de-ba20-4b2dc840724e | -3.46874 | -50.08056 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40175534-d039-3c22-b007-f94eaec6f322 | -8.08488 | -55.28891 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fef50d07-bf92-3e61-afe4-25ed3a157687 | -3.03197 | -53.91295 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3114a9b-0c6a-3575-9ec8-93a74a7fdcfa | -3.0137 | -53.91011 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ffc1cae-d955-3736-98fe-1f97213350c8 | -2.8525 | -59.11074 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74299b9a-e0a2-3fbd-8887-a75da7c4fb05 | -2.95133 | -54.20387 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ab031b4-05b7-3bc6-b25f-6ac6d55493f5 | -11.45642 | -43.38437 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5b6ae7b-eab7-36ad-8c53-9b8f4dbc84c0 | -2.76698 | -54.09187 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c99bc934-fbc4-35ef-a952-8acab2e566e9 | -5.47013 | -49.04223 | 2026-10-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 921f480b-664c-3eb3-8d3e-b817d13d81d5 | -3.00855 | -54.13133 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f01c724-9dd7-3cd0-8064-3a5119a3e53e | -2.94148 | -54.17061 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4490a431-c8aa-332b-80c0-ce68099d7558 | -8.21928 | -46.33641 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 46668fa6-ea81-36be-b491-b0bb44a538c3 | -2.783 | -54.06285 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 244262b1-e071-3d28-bb4b-e58394ae1df4 | -3.92758 | -54.57756 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 250a7b77-b7c7-3617-b872-4a67f57902a9 | -5.73731 | -53.62195 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa4d997f-1eb6-3905-bf1b-3bd473eae2b1 | -3.17737 | -54.60846 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d4d9c7c-9f2c-3c41-8d0d-9aa29aa5c0dd | -7.80452 | -46.85225 | 2026-10-08 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85516dc6-373e-33ee-a278-6e87e6ae9627 | -3.17358 | -54.60784 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82ee3511-7700-3200-b6c0-076eb43fc708 | -4.62009 | -56.17201 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7027b82d-7c1f-3dd0-b80c-be14503a21be | -5.74139 | -41.75574 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9aee289d-0d47-3758-b6cd-0d18ac2afd93 | -3.4682 | -50.08401 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de03b527-bd36-3d41-8b27-fe3cad672545 | -3.27804 | -54.06208 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6aa9599-2742-37b0-acaa-d5e28f69aded | -3.06149 | -54.3852 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 805314cf-2bce-3ab1-938c-28b56a14aa01 | -6.11636 | -51.73536 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b55163c-347b-37e7-adb9-7f714dd38952 | -6.79112 | -41.25206 | 2026-10-08 04:46:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d65d442-656c-35a5-809a-d678df97b281 | -3.0675 | -54.25224 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README107.md)
