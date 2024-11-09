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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01663f2f-b5bd-324e-b087-6a9dfc652203 | -1.5347 | -52.1899 | 2024-11-09 06:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 2fe7c914-6e9f-31b8-a60d-df6a334b3d57 | -1.5347 | -52.1899 | 2024-11-09 06:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f4fd5844-0a6d-36fc-902d-987f68f6d12d | -3.6004 | -47.3395 | 2024-11-09 06:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| ffa9f7f5-f9c4-38ac-9594-c23ffef50a0d | -1.5163 | -52.1901 | 2024-11-09 06:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 06408ba5-569e-3e6d-a37c-a4f1f4db4e55 | -1.5163 | -52.1901 | 2024-11-09 07:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 823699c8-c3fd-36d0-ad42-65db1aac22dd | -1.5347 | -52.1899 | 2024-11-09 07:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4c43844f-e480-36c1-9e08-cb1f8a7147b4 | -3.2211 | -45.2024 | 2024-11-09 07:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 888e6358-989a-3a90-81ef-5ceeb03354ae | -1.5163 | -52.1901 | 2024-11-09 07:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a7c092db-e6fd-37f3-9796-22159442d262 | -1.5163 | -52.1901 | 2024-11-09 07:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6aba3b18-ecbd-30a4-b84f-9885872ca291 | -1.5347 | -52.1899 | 2024-11-09 07:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 15cc871c-b5af-3469-9b94-775cf2f7ec47 | -1.5163 | -52.1901 | 2024-11-09 07:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5f37a39c-db96-3ae6-9fcf-e1aa585dd114 | -11.09 | -43.36 | 2024-11-09 08:00:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29187d44-6908-3135-a322-cdcacb700a15 | -11.09 | -43.31 | 2024-11-09 10:00:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 265982f7-125b-3a29-a69a-c9e31282bbd7 | -11.09 | -43.36 | 2024-11-09 10:00:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc950214-7dfb-3931-b6da-6400dc0bce91 | -0.989 | -47.6244 | 2024-11-09 10:40:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d794ddd3-fde5-364f-a099-133ff8fffc16 | -1.7472 | -47.678 | 2024-11-09 10:40:00 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| cdeac3b9-a4d6-3623-8787-23787824aefb | -1.5623 | -47.638 | 2024-11-09 10:50:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 172b9531-e26e-3194-9a4e-15aadcce3d91 | -1.6319 | -49.5869 | 2024-11-09 10:50:00 | GOES-16 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 14ffe637-8f99-3ced-be1f-6cfd7ea6b196 | -1.5808 | -47.6376 | 2024-11-09 10:50:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 46c9f7f1-a79c-350c-922a-15dc9e5584ef | -0.989 | -47.6244 | 2024-11-09 10:50:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 15627010-8616-3551-a4ec-c2ba330c8cc7 | -2.4104 | -48.5265 | 2024-11-09 11:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 0ae14270-d7b3-3390-89ef-0e5fadbf6867 | -2.4104 | -48.5265 | 2024-11-09 11:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 321b82f1-08a6-39b5-82a5-fe7eebb0f5c1 | -2.4104 | -48.5265 | 2024-11-09 11:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 839cc97f-ecdf-36ee-9f25-e907b34f1e84 | -3.536 | -42.0897 | 2024-11-09 11:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 6533b01f-8972-3c28-980b-303366a9dcb2 | -3.5361 | -42.066 | 2024-11-09 11:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 177.4 |
| 4556ffff-1409-3678-8b4e-dd81b84725bf | -3.536 | -42.0897 | 2024-11-09 11:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 20ca12db-5993-3c0f-bc6b-302f49061190 | -3.5361 | -42.066 | 2024-11-09 11:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 151.7 |
| ec61e19d-2903-3126-92ef-1c489999465c | -2.4104 | -48.5265 | 2024-11-09 11:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| c3af1497-16bc-34ed-a8eb-60b2be059f84 | -1.5163 | -52.1901 | 2024-11-09 11:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e68c76c1-e860-3eff-b10b-60500f3910fb | -1.5163 | -52.1901 | 2024-11-09 12:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e920059b-6995-3aad-be21-c74ddeb25736 | -2.2479 | -53.7627 | 2024-11-09 12:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 44998587-27f9-347c-88cd-2757c89b8593 | -2.2479 | -53.7829 | 2024-11-09 12:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| f14d58f8-6e7b-3447-86db-c1f4782affdf | -2.2295 | -53.7832 | 2024-11-09 12:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 280.0 |
| a4b05e95-43cf-3562-a153-4f95bc3c52f1 | -3.5361 | -42.066 | 2024-11-09 12:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| e4e39ec4-62a3-375a-bd08-7801c3500efe | -2.4104 | -48.5265 | 2024-11-09 12:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 6540c93c-0faf-3228-8a4d-f1699e1ae67a | -1.5164 | -52.1696 | 2024-11-09 12:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4f7049b4-d998-3402-8e4e-4416cc595186 | -2.2295 | -53.7631 | 2024-11-09 12:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 165.8 |
| acc7dcf1-da7f-338c-b2cb-b29d80a68880 | -3.6839 | -42.3665 | 2024-11-09 12:10:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 7fbcca91-d70b-3d24-955a-2b974dd864b4 | -2.2479 | -53.7829 | 2024-11-09 12:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 316.8 |
| c3f03781-2580-31a8-921b-ecd130437c69 | -3.6652 | -42.3675 | 2024-11-09 12:10:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 162.0 |
| f814d400-27ce-3892-ad13-f7378035f787 | -2.2479 | -53.7627 | 2024-11-09 12:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 182.6 |
| 79b74081-cc43-3c64-a5d7-e040d5a6aa41 | -0.9891 | -47.6026 | 2024-11-09 12:10:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 976d1c35-af5d-3299-a129-b46d4da9ed5c | -1.5164 | -52.1696 | 2024-11-09 12:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| be6f44bd-daa3-3a8a-a79c-c2a7128980d1 | -2.4104 | -48.5265 | 2024-11-09 12:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| fc70e953-b466-3049-83d4-02d86453083b | -2.4105 | -48.505 | 2024-11-09 12:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| aab44001-a26e-37df-b541-98757999ecf4 | -2.2295 | -53.7631 | 2024-11-09 12:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 8c82f84c-2355-319b-bb7a-2aa1b05ad0b7 | -0.9891 | -47.6026 | 2024-11-09 12:20:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 265.5 |
| b60ad2a1-06b0-3c3e-86fe-003b5c7d205b | -3.6652 | -42.3675 | 2024-11-09 12:20:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 182.1 |
| 0da4b339-1e3f-30bd-83da-8079792a67e8 | -1.5164 | -52.1696 | 2024-11-09 12:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| e087286f-06bf-3567-af57-78c1c3c14595 | -3.6839 | -42.3665 | 2024-11-09 12:20:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| 677c7486-1536-3b03-ab48-181c4537cdf8 | -2.4104 | -48.5265 | 2024-11-09 12:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 573e84a3-49b9-39de-a710-0f6d1f74376c | -2.2479 | -53.7829 | 2024-11-09 12:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 276.0 |
| adc631e6-437b-31e1-9109-ae740f2e1af5 | -3.3652 | -50.1342 | 2024-11-09 12:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 2dfa06b9-6690-3c80-93ea-4931bec87e4a | -3.3673 | -42.1691 | 2024-11-09 12:30:00 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 93f6ee48-4926-3537-800c-6fa43520bef2 | -3.9669 | -48.1716 | 2024-11-09 12:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 74164a73-0c6c-3ddd-971d-cf3a599eae84 | -2.4104 | -48.5265 | 2024-11-09 12:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 6d2afcd0-0d26-3906-952c-a970288263b8 | -5.4548 | -43.2426 | 2024-11-09 12:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| cc33b684-83d2-3adf-87aa-e76ae34124cf | -3.9668 | -48.1932 | 2024-11-09 12:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 25ccd197-4920-3ecf-b7ed-af9b90933bf6 | -2.2479 | -53.7829 | 2024-11-09 12:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 345.9 |
| cf699113-f369-3960-acb1-87ba73c5b40c | -0.9891 | -47.6026 | 2024-11-09 12:30:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 50d163b0-2cf0-38f8-a702-aca6ece4f6db | -2.2479 | -53.7627 | 2024-11-09 12:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 496b1864-9df6-303f-a5bb-d199ffa11a1c | -5.4544 | -43.2893 | 2024-11-09 12:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| b26f8c38-d876-3fe3-b41c-79b89eddd8c3 | -1.4144 | -47.6187 | 2024-11-09 12:30:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 999651ca-45a0-3f9a-afd6-95bb08cacb11 | -2.2295 | -53.7631 | 2024-11-09 12:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| f727e620-5a72-362c-8d16-1f1f59fc7919 | -5.4734 | -43.2646 | 2024-11-09 12:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 85d9164c-f056-3e86-8451-618c0c070c49 | -5.4546 | -43.2659 | 2024-11-09 12:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 238.3 |
| b450e029-4c62-3d48-a368-bfd2753114b9 | -3.5462 | -43.5663 | 2024-11-09 12:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 86524b98-beab-3dfb-9b2e-9e811303bd38 | -5.4359 | -43.2673 | 2024-11-09 12:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c462a773-f1e7-3cc6-b1f4-5d42e84e07c1 | -1.5164 | -52.1696 | 2024-11-09 12:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 0b8ed8bb-707b-35a6-a523-b3fd157e93b0 | -1.5163 | -52.1901 | 2024-11-09 12:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| dc9f5dc5-8b50-35ad-a3b9-a0fc90bbe814 | -3.6839 | -42.3665 | 2024-11-09 12:30:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 117.1 |
| f0533c67-425a-3d44-bad7-fadb290a5f58 | -5.4548 | -43.2426 | 2024-11-09 12:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 384fdbf7-3eae-3747-b3b5-e7c4b80dd5b6 | -3.9669 | -48.1716 | 2024-11-09 12:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| e10fd810-315a-3bff-8985-51598a614471 | -3.6652 | -42.3675 | 2024-11-09 12:40:00 | GOES-16 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| ecd9150f-6fbe-3f74-900c-74fd7bf65155 | -1.5164 | -52.1696 | 2024-11-09 12:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 5b7f20a3-1ec8-32d6-b4c4-dbfe628ed503 | -2.455 | -46.3235 | 2024-11-09 12:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c873faca-b00e-3fec-be34-7d980841e0a3 | -0.9891 | -47.6026 | 2024-11-09 12:40:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 3f0ae8dd-ea4f-3dfd-a07a-764b65c8040e | -2.4104 | -48.5265 | 2024-11-09 12:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| d94d0935-ec0e-3802-aaa6-d560193df16b | -0.2299 | -51.6455 | 2024-11-09 12:40:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 61c805c1-73da-3265-848d-68f7524cc382 | -5.4546 | -43.2659 | 2024-11-09 12:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 468b7220-42a8-31bb-b1fd-f47eaa3f3ffd | -3.3673 | -42.1691 | 2024-11-09 12:40:00 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 3c0d218b-4194-3462-878d-e9f42677dcdb | -5.4544 | -43.2893 | 2024-11-09 12:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 1ae68c20-5f44-325f-93cf-fb8997488189 | -5.4734 | -43.2646 | 2024-11-09 12:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 77a906b1-2762-38a1-8e45-dc1fa0467299 | -5.4359 | -43.2673 | 2024-11-09 12:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 1c40c4f9-254a-3ca1-8118-24bfa82c0a54 | -3.4803 | -42.0212 | 2024-11-09 12:40:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 141.7 |
| 78f07a0f-abc1-3a0f-9447-a837839c2407 | -1.5163 | -52.1901 | 2024-11-09 12:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 910f625e-0e61-397b-afc9-3703d693f820 | -2.379 | -46.8552 | 2024-11-09 12:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| a3dc0199-020d-3292-953e-7d5b29bba5f9 | -3.9669 | -48.1716 | 2024-11-09 12:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 2d678f45-4375-307a-b5d2-bd922eb3d410 | -5.4546 | -43.2659 | 2024-11-09 12:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 223.9 |
| bd54fe3a-594b-38ea-b83b-109d3970630b | -3.6004 | -47.3395 | 2024-11-09 12:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 56b1d4ca-246e-314c-80d0-4b4c8345a455 | -2.455 | -46.3235 | 2024-11-09 12:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 8a0a938d-2dcc-339e-867c-405e0cba8e46 | -5.4548 | -43.2426 | 2024-11-09 12:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 4e5e95c4-a680-328a-a94b-4ad702de3307 | -3.5462 | -43.5663 | 2024-11-09 12:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 75aff269-723f-3183-9ac6-de7f32fb4339 | -5.4734 | -43.2646 | 2024-11-09 12:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| c0f25326-4a06-30b2-a53f-73529c972820 | -5.4544 | -43.2893 | 2024-11-09 12:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| f7fefe6e-5e9a-305e-80ea-ef566cbe58e1 | -1.5164 | -52.1696 | 2024-11-09 12:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| aa93a1fc-efb5-3324-9ce4-4e70fdcc1c87 | -5.4359 | -43.2673 | 2024-11-09 12:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 05246fe7-2604-3da7-b6a2-1bd9a8420490 | -2.4104 | -48.5265 | 2024-11-09 12:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ed0f3b12-1425-3941-a60f-5cb47434cff0 | -2.2479 | -53.7627 | 2024-11-09 12:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| cd61bb30-14c8-388c-ba34-cdb7913d3f4b | -2.3605 | -46.8557 | 2024-11-09 13:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |


[Clique aqui para ver as próximas entradas](README119.md)
