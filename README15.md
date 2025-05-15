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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b481c0a-4141-37bf-a7f6-af88e6c3db91 | -12.3522 | -49.94 | 2025-05-15 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 9046ed15-b367-3c77-8e2a-0cc818b98542 | -6.1792 | -48.0494 | 2025-05-15 13:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 56add76f-deeb-3bd4-8b24-a4c17d9985ba | -12.3519 | -49.9617 | 2025-05-15 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 211.3 |
| e4ea96f9-0e42-3d4a-be9a-211bc2c24339 | -11.0789 | -46.1245 | 2025-05-15 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a95bb730-9d7e-363e-bd85-ccc0fcb76be4 | -12.3519 | -49.9617 | 2025-05-15 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 59de47fb-bedf-3176-9a01-338caafd47df | -9.6825 | -49.6995 | 2025-05-15 13:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 02c09626-10dd-3c79-96b5-66368d0ea0dd | -12.3522 | -49.94 | 2025-05-15 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| eb795daa-11d1-35df-bb7d-56f94307ea3b | -6.1792 | -48.0494 | 2025-05-15 13:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 0b4331ef-ea12-39d5-bcbb-9f8dd2995a6f | -11.6199 | -48.0226 | 2025-05-15 13:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d4180b36-5a21-3164-85f0-bf3fec66b8c6 | -9.6825 | -49.6995 | 2025-05-15 13:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| dc9c8452-a861-3de9-b58a-4e07ffba60e1 | -12.3519 | -49.9617 | 2025-05-15 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 8c833186-b1c6-389d-8355-13a77c708113 | -9.6822 | -49.721 | 2025-05-15 13:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c3a252a4-c194-31a0-85ce-a1f3e56c5499 | -12.3519 | -49.9617 | 2025-05-15 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 8998ae48-68d0-3a12-8422-8c98028a4e2c | -7.5573 | -43.3866 | 2025-05-15 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d92a5d1c-5cce-3306-b2bc-bf186086c77c | -13.5683 | -52.8783 | 2025-05-15 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ff2c7b1a-a916-318c-a1cb-27823c478cb5 | -11.6199 | -48.0226 | 2025-05-15 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 35d5baa2-d23c-3c58-b827-332d3ddeb6d5 | -12.3522 | -49.94 | 2025-05-15 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| dec26e54-3c5b-310c-8aa3-211f689e743b | -10.6802 | -49.9187 | 2025-05-15 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| afa158a1-6d37-3ca0-9580-53ef42bb41db | -12.3522 | -49.94 | 2025-05-15 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 61bf47ac-31f0-3cdc-a33a-6a2926cfbae6 | -12.3519 | -49.9617 | 2025-05-15 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| a1d6db62-9e59-3c3f-a078-a72ed0e0c10d | -13.5683 | -52.8783 | 2025-05-15 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 62c6d41e-af09-34ab-b08e-b8305c490a8d | -7.5762 | -43.3847 | 2025-05-15 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| ea25716b-3f2f-37bc-b314-f46024006e64 | -10.6988 | -49.9382 | 2025-05-15 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| c2c446ad-48c1-3aaa-a9f9-9631117e9bee | -7.5573 | -43.3866 | 2025-05-15 13:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a10b989d-d036-3346-9995-9d26a1a5c8a0 | -11.6199 | -48.0226 | 2025-05-15 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 9a892549-870e-3fb9-9c7b-e06b7b5d9986 | -13.5683 | -52.8783 | 2025-05-15 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| eb9f2779-2b10-30d5-a6ee-16ecab1e06ca | -7.557 | -43.41 | 2025-05-15 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 9fbd6eb1-1406-32c4-a267-d80a5246dfc5 | -12.3519 | -49.9617 | 2025-05-15 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 16db3a43-4354-302f-a2a6-e479cd735bbf | -10.6802 | -49.9187 | 2025-05-15 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 19f473df-7b3d-391f-bb04-7c59341a1a3b | -7.5573 | -43.3866 | 2025-05-15 13:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 9ae89814-f114-34e9-a7dd-679478b99a23 | -7.5573 | -43.3866 | 2025-05-15 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| be00b540-dcfa-3bc8-abc9-618ed6543e03 | -7.5762 | -43.3847 | 2025-05-15 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 9bc08e28-46d9-3ef5-b355-d1a7927ba37b | -7.557 | -43.41 | 2025-05-15 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| ee5f87dd-a4e1-3730-8221-fd16d916d877 | -11.8027 | -49.7263 | 2025-05-15 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| adf6b10c-7e87-3e93-943b-dccf4e25e68e | -11.6199 | -48.0226 | 2025-05-15 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 2e19064b-ec36-36ce-9ba8-23489b2d7530 | -13.5683 | -52.8783 | 2025-05-15 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 45e9ac4e-2ff4-3e71-98fc-dfceed1e9c25 | -12.3519 | -49.9617 | 2025-05-15 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 5d60e681-8719-3ebf-b719-0e5685a0a8c4 | -12.3522 | -49.94 | 2025-05-15 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 57e5bb3b-4840-3f6a-9a8f-e5f2f970b3e9 | -11.8218 | -49.724 | 2025-05-15 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| ddcce302-9f7e-35f0-bad9-5ff2b0f7b8ad | -10.4721 | -49.9194 | 2025-05-15 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 8f747fbd-b3fe-3148-ad83-177270e65b78 | -12.3519 | -49.9617 | 2025-05-15 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| db8a87ee-9998-35ea-94c0-92bd51df6a66 | -12.3522 | -49.94 | 2025-05-15 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 1c5964e0-d9ba-3bf2-917c-b50e2b59e1d9 | -13.5683 | -52.8783 | 2025-05-15 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| b2488355-20ea-3c77-8618-117e97e2a618 | -10.8379 | -49.4706 | 2025-05-15 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 55f874bd-6c98-3255-973d-66ae73cd0ed0 | -10.6988 | -49.9382 | 2025-05-15 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 3c49776e-4910-34bd-87b6-a58c20b8be3a | -10.8379 | -49.4706 | 2025-05-15 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 3b289e37-f4ea-3b1a-8143-2a5a31356585 | -10.6988 | -49.9382 | 2025-05-15 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 404456ad-a7b1-32bc-a7aa-a6068afe80fd | -12.3519 | -49.9617 | 2025-05-15 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 1774496e-5a12-3675-a3c4-42d43b7f4f15 | -10.6988 | -49.9382 | 2025-05-15 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 95c67a19-3152-394b-a263-9e9d9a577366 | -12.3519 | -49.9617 | 2025-05-15 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| e463a6c3-5887-33a4-9e8a-46064aba54b3 | -13.5683 | -52.8783 | 2025-05-15 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 72c9b2ab-7871-314e-b9de-55450c5f8ff0 | -10.8379 | -49.4706 | 2025-05-15 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 397a69d8-9849-31f7-8d61-4eb393a4bf8e | -10.6988 | -49.9382 | 2025-05-15 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| f641560a-6fa8-37b0-896e-55e0f815bf3b | -12.3519 | -49.9617 | 2025-05-15 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |


