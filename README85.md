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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff47e538-cbcd-3fbc-a5f4-9a8550eb3461 | -8.5406 | -54.8197 | 2026-08-22 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| fc486b55-f43f-3c6e-a7c2-a6fb730f848c | -6.254 | -55.391 | 2026-08-22 12:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b685c38b-3cea-30fa-a8cd-1f1e6874cebf | -11.3801 | -46.3558 | 2026-08-22 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 8e8f4911-2190-3ada-bb93-7ca5636897eb | -11.6059 | -46.551 | 2026-08-22 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| ff278850-ef7d-33e3-b0c2-ae6a410efec7 | -8.9658 | -49.8741 | 2026-08-22 12:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5a282aa8-fe28-3633-8cbe-79732507134b | -8.5406 | -54.8197 | 2026-08-22 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 6277626d-ad46-3e77-8f83-f58867514889 | -11.6055 | -46.5736 | 2026-08-22 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| a3903317-596a-3eed-9c58-3dff8a327e7a | -13.5481 | -51.7403 | 2026-08-22 12:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| c530ae07-3431-3e92-beb7-43a04b05dde6 | -6.7692 | -58.6679 | 2026-08-22 12:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 453e1eb1-ea33-3128-a2ec-56b1e9404fc8 | -11.4494 | -44.5353 | 2026-08-22 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 528.3 |
| 26975acf-10f5-3b5a-80d1-c095a49ee586 | -6.7878 | -58.6477 | 2026-08-22 12:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 8a77f2da-e50d-3a4d-b15d-3aa0757f66b7 | -11.449 | -44.5587 | 2026-08-22 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| bb5e7fd0-f889-3f56-a2f4-ba97326d7153 | -6.8018 | -59.4201 | 2026-08-22 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 0cdba9c2-3521-3822-a478-f79a3f3df125 | -8.522 | -54.8209 | 2026-08-22 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 3a78dba2-1740-3b09-b897-f3243e0ba9af | -6.8568 | -59.4757 | 2026-08-22 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| aceafbb3-949b-3c0f-aea1-64c072f0c411 | -12.2806 | -43.1813 | 2026-08-22 12:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 116.5 |
| 2b104993-4083-3e83-9d6d-25ce92da054a | -12.281 | -43.1574 | 2026-08-22 12:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 144.2 |
| 43134a84-9f17-3281-bd33-82200a627426 | -6.8569 | -59.4564 | 2026-08-22 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| deeaad96-6466-315b-aa32-fb1145422423 | -17.6092 | -44.6119 | 2026-08-22 12:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 320a2001-78c9-363f-a641-c35e792456de | -8.1574 | -46.7247 | 2026-08-22 12:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| a1513af3-d21b-3685-889d-8e68ed96e1e7 | -11.625 | -46.5484 | 2026-08-22 12:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 914864e0-eede-3b5f-9481-d874c9bed8c2 | -6.8569 | -59.4564 | 2026-08-22 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| d3a8f550-efd5-3d71-ab0f-b606ced21ba3 | -6.8062 | -58.6469 | 2026-08-22 12:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 5595f469-0548-3082-ac5a-d1d909e95b21 | -10.9624 | -51.4214 | 2026-08-22 12:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 1984aac0-c67a-3461-8343-b0d2a1192066 | -6.254 | -55.391 | 2026-08-22 12:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 2d55ba3d-fa07-3d00-997c-05f317e1582b | -12.281 | -43.1574 | 2026-08-22 12:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 120.2 |
| 36183c9e-9dfd-3b3a-bfdf-759b5397c74a | -6.8018 | -59.4201 | 2026-08-22 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 87c487be-60b9-3606-9c7f-6c598d93922e | -12.2806 | -43.1813 | 2026-08-22 12:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 90.2 |
| 5d6f5109-f05b-3960-a737-cd41818defe9 | -6.8568 | -59.4757 | 2026-08-22 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| b3b3ee6a-8251-3a4e-850e-84f8516a6a09 | -13.6995 | -51.87 | 2026-08-22 12:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 78b77540-688c-3f49-b4d9-28d8eb6d868a | -11.6059 | -46.551 | 2026-08-22 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 229.1 |
| 061587f0-6980-3d7e-b3f1-dadb21509374 | -8.522 | -54.8209 | 2026-08-22 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 9a016a9f-e921-3b8a-a81d-1cb019cd3988 | -8.5406 | -54.8197 | 2026-08-22 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 35f77ed2-a2f7-30fc-aaa5-5f64dad8897b | -11.6055 | -46.5736 | 2026-08-22 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 4a83d9b0-5470-35b7-8962-9ade19f9e243 | -17.6092 | -44.6119 | 2026-08-22 12:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 66feee19-7609-32a8-9460-9f78d08836e9 | -11.449 | -44.5587 | 2026-08-22 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| c865f72d-14f4-306a-96cc-70a9c813bde3 | -11.625 | -46.5484 | 2026-08-22 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 162.8 |
| e34637b1-2fa4-36a7-ac5a-f4cb3f05f9c7 | -7.3625 | -55.673 | 2026-08-22 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d4c1ae85-be0e-35ab-b566-aa4bcc6fd9f0 | -11.4494 | -44.5353 | 2026-08-22 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 484.0 |
| 4b2f0b34-1089-35ca-aeda-c0680be1f696 | -13.6999 | -51.8487 | 2026-08-22 12:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 91c51eea-ab82-39a1-9972-d3ce5f689fb1 | -11.6063 | -46.5284 | 2026-08-22 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 6882d0ff-8d78-3fac-9938-b1993c0b56c0 | -6.7878 | -58.6477 | 2026-08-22 12:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| e0ad9f49-b86d-3e31-8f24-08fdde954ed8 | -6.7692 | -58.6679 | 2026-08-22 12:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 316a1c07-e675-32f0-a575-006883135907 | -13.5481 | -51.7403 | 2026-08-22 12:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 917c4dd1-55d3-38a4-a8b2-be6e3adf0557 | -8.5404 | -54.8398 | 2026-08-22 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 03970565-4958-328c-887a-f1af4ecdd885 | -12.8362 | -48.4567 | 2026-08-22 12:30:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| e7c86513-f971-3de7-9aff-ddd10c55e68f | -9.1722 | -59.4629 | 2026-08-22 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 9f5d8e78-e3bb-3bf0-9dc2-c27478fd17c2 | -8.4739 | -46.9831 | 2026-08-22 12:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0744fcc8-2826-3547-8e38-c91d039f8df0 | -11.6055 | -46.5736 | 2026-08-22 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 137.2 |
| aea67129-2d29-3001-8b7d-f78fcce8c29c | -11.5868 | -46.5536 | 2026-08-22 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a13f1f8a-eb5b-364a-a00e-b1742a930926 | -6.8568 | -59.4757 | 2026-08-22 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| dc304a51-9b2a-368f-8ec4-186bef3c90bf | -6.8062 | -58.6469 | 2026-08-22 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 94417d31-5902-3aa2-a397-cf89c5cdfc8b | -6.8569 | -59.4564 | 2026-08-22 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 22dca93f-5049-314f-967a-674af1d5dec8 | -11.3663 | -46.0405 | 2026-08-22 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| f88b9505-aaa3-3a54-94f4-7245e2da80eb | -6.8004 | -59.6704 | 2026-08-22 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 23391c65-3446-3ae0-9ef9-b6b1bdeee6fd | -7.0191 | -48.0323 | 2026-08-22 12:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 34882aa7-31c9-3d9f-bae6-554cc9ed1776 | -13.5481 | -51.7403 | 2026-08-22 12:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 24355a2b-3e20-36d0-9102-1bf58e534ebc | -6.254 | -55.391 | 2026-08-22 12:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 51944f32-8272-3a57-8365-0ae8c7d0ba81 | -8.5218 | -54.8411 | 2026-08-22 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| de8b908e-3f59-34e0-bd29-2fae2b94889f | -8.5406 | -54.8197 | 2026-08-22 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| c17f5d52-12ee-366e-a737-14d6351b2e5d | -10.9624 | -51.4214 | 2026-08-22 12:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 805958f7-ee58-3523-ad8a-25ddabddeb2d | -12.2806 | -43.1813 | 2026-08-22 12:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 119.5 |
| ea9be709-9821-3b7a-9c64-e493bc9b0e63 | -10.9435 | -51.4234 | 2026-08-22 12:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 8f1e0304-2eab-362c-8b48-d9f080154d5a | -11.625 | -46.5484 | 2026-08-22 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 0fa95e95-3ca4-3587-9bee-1181873699d8 | -11.4494 | -44.5353 | 2026-08-22 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 311.9 |
| 39976a8e-ad4b-3288-ab1d-c25a362ac293 | -8.5404 | -54.8398 | 2026-08-22 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 626723a1-e5d1-3081-89f2-7f1b15e2b2b9 | -9.1724 | -59.4436 | 2026-08-22 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 258e1928-64ef-33de-a5d0-a7db203a3761 | -17.6092 | -44.6119 | 2026-08-22 12:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 105.7 |
| a81b1150-0a2a-36ee-92f4-a09a7f315159 | -6.7692 | -58.6679 | 2026-08-22 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 1eee2a59-1b1c-3f1c-b897-7ad8f3dae7d7 | -11.6059 | -46.551 | 2026-08-22 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 212.3 |
| e59b1b25-a8b5-3504-a765-5ab8c9263053 | -6.8018 | -59.4201 | 2026-08-22 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.3 |
| ea5a06b6-47cd-3ef5-889c-a715fc65e61f | -17.5891 | -44.6164 | 2026-08-22 12:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9d79012f-f7bc-3108-870c-e78fde173afd | -11.3854 | -46.0378 | 2026-08-22 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 179eaf35-7990-356c-8c6f-a8c47558bcb8 | -8.5221 | -54.8007 | 2026-08-22 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 5effe2a8-a2a5-3b78-8b29-8a13f9b02c1c | -8.522 | -54.8209 | 2026-08-22 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.9 |
| ddd192e4-4d57-3edb-9c25-f9381a3526c0 | -11.4298 | -44.5615 | 2026-08-22 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e7766d5f-f0c8-31f7-b3a7-5d96266ab316 | -6.7833 | -59.4208 | 2026-08-22 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 94eccd23-4735-3857-8182-2846640be8ae | -9.0346 | -45.8735 | 2026-08-22 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| aed31888-c1e5-3447-bd6a-12580937a2e8 | -11.5864 | -46.5762 | 2026-08-22 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 3af4ce3d-c3eb-33df-ade7-ab77cfd1a652 | -9.1722 | -59.4629 | 2026-08-22 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| c50b60f6-4fbc-3501-b9b6-59592594e24c | -9.0535 | -45.8715 | 2026-08-22 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f0f6bd98-025e-3ff2-aabf-614f15f90d1a | -12.281 | -43.1574 | 2026-08-22 12:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 155.2 |
| 1a49ab27-8a9b-3e23-8fda-62b67d023613 | -6.7878 | -58.6477 | 2026-08-22 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| f26ddc4d-aa0c-3b24-bfb8-042c240783e8 | -6.8063 | -58.6275 | 2026-08-22 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 505e5554-a7dd-345e-a967-a832bd9ea689 | -17.5891 | -44.6164 | 2026-08-22 12:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 4cbd9901-cdfe-332e-a2b0-147cc0b8cb27 | -6.8188 | -59.6696 | 2026-08-22 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| a035b974-31fa-3428-ba2f-0adbfd407f67 | -7.0004 | -48.0338 | 2026-08-22 12:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 1a17f934-f0b2-3ec0-a1eb-02a895c491b1 | -6.7691 | -58.6873 | 2026-08-22 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 882cf82e-9c17-3464-bfbb-b5124ba6e47b | -11.4498 | -44.512 | 2026-08-22 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 241e2003-a17a-3d14-bc0f-7c9c0abb5c71 | -10.9624 | -51.4214 | 2026-08-22 12:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 142.5 |
| c58d2fd9-01c1-3f22-9e11-020f0f479d4a | -6.7692 | -58.6679 | 2026-08-22 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 2297aae1-1918-3d35-9a79-45178b2453e7 | -11.5864 | -46.5762 | 2026-08-22 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 0081422f-2c81-3ba6-94a1-a1a9a4c2628b | -11.6059 | -46.551 | 2026-08-22 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 301.6 |
| 620f7c91-2d59-3359-84af-fa3f63c672dc | -9.1722 | -59.4629 | 2026-08-22 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 95a9a35b-7619-377b-b4ad-b48b5107eef6 | -9.0346 | -45.8735 | 2026-08-22 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f7c220eb-85b4-38ab-b345-73ca9ace8d44 | -11.6055 | -46.5736 | 2026-08-22 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 82cb8623-0e93-3024-9bec-f1d51c820538 | -6.8004 | -59.6704 | 2026-08-22 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| df2b482f-f147-3845-a200-d1ea8a781907 | -6.7832 | -59.4401 | 2026-08-22 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| edfb0711-050b-3932-9770-cb522e2d7cbf | -11.5868 | -46.5536 | 2026-08-22 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 179.1 |
| eebe5d30-47b4-3f6a-8ad3-c3c13f960731 | -8.522 | -54.8209 | 2026-08-22 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |


[Clique aqui para ver as próximas entradas](README86.md)
