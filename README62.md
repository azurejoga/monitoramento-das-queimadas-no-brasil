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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c42b820-ba12-380d-ac52-c8bb9df5d219 | -3.41911 | -58.2109 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e82f8d25-0107-39d3-9219-e63cfe71f1c2 | -5.12761 | -55.95751 | 2026-09-14 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb979440-e8f5-3cdc-b1e4-b17ff1c818d8 | -2.66514 | -57.54278 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c067a05-6468-3e3a-9061-236c4d835644 | -3.35553 | -59.62556 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8af53763-91af-382e-a7da-cafa7482a834 | -2.67716 | -57.56077 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ae3762ed-41b2-3beb-8556-8970df1f7b59 | -3.17312 | -58.64995 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4b4aa33-9d11-3683-a870-5d86e5af5763 | -6.11425 | -57.67827 | 2026-09-14 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5d3aaf5f-3f87-3d4e-9a26-ad9b6f2d7eef | -2.67849 | -57.4979 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a17913f-41e0-341f-a3b9-9449aa1473ef | -2.67394 | -57.57001 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11b61d00-1adf-3a95-bdd0-a3ffb71207c7 | -2.48181 | -58.00422 | 2026-09-14 06:12:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e512a7cf-4d84-3690-a8f6-06fb3374b054 | -4.12706 | -60.68811 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7edb6243-35f1-38a5-ac83-340bb4edb4dc | -3.71559 | -58.86559 | 2026-09-14 06:12:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b07f678-512f-3217-8cbc-0dfef68d1d73 | -2.66669 | -57.54361 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cb521577-1ffa-3b24-865d-904bbd0e9716 | -2.67567 | -57.57091 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d5f094ef-c220-36d6-aa80-ed68c529db81 | -4.12798 | -60.68164 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 75fed4c3-3a12-32e6-bc83-0900fcd28174 | -2.66591 | -57.53771 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85bdd196-42dc-3902-bce3-c072cf1c508a | -2.66743 | -57.53853 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b10e384d-723c-327d-879e-aa0c477dadd1 | -6.11503 | -57.67257 | 2026-09-14 06:12:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dbea2bd9-7dbb-329d-bc75-de85564575bb | -3.60256 | -59.06948 | 2026-09-14 06:12:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c9624183-1218-39c7-a42d-5d5422586f2d | -2.67148 | -57.54375 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80a301b0-6fc1-3e17-8381-fc6500b125a1 | -3.41756 | -58.21344 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e500b8d-4c01-3134-abad-1783d1c48f57 | -2.70476 | -57.5494 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a10ad136-5ad8-3dd7-89f9-dcd3ea07be53 | -2.67225 | -57.5387 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b28d385d-2fb1-3271-9f09-8f75da8e054b | -2.67378 | -57.53952 | 2026-09-14 06:12:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 324f19c2-bf6a-3917-8066-e1831e68d6fa | -4.12897 | -60.68571 | 2026-09-14 06:12:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8b8f35d2-9651-38eb-8078-1c4753ba45b2 | -3.17636 | -61.11691 | 2026-09-14 06:12:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d79f2e8-ad72-3d29-af4b-a063cd527cad | -3.17037 | -58.65253 | 2026-09-14 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe5768a1-2375-3125-9da0-99f314a0eb78 | -6.28953 | -59.9354 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7fbb545-8725-3471-82d2-f59d2a8ac53c | -6.74913 | -59.43119 | 2026-09-14 06:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1a9510e-33e3-3591-be58-ef91ea7e9754 | -6.29883 | -59.95267 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| beb38b05-6268-327f-a134-cf44af9a2e4d | -6.27808 | -59.93358 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27784670-e6cc-302d-9e5d-9ccbf87fd99c | -6.27193 | -59.92591 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95fed718-a113-309b-ad4d-c0025ccebb0c | -6.59257 | -58.85448 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ba16897-c66a-3682-8880-01788474476a | -6.74593 | -59.43256 | 2026-09-14 06:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cabccc84-21a2-3fbf-a8c7-1ea539747772 | -6.64651 | -58.82224 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b63b6658-922b-3356-a110-4ad90bc61c33 | -6.78986 | -62.97987 | 2026-09-14 06:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fb85109-a8ac-3b4b-9e83-ed075c98f690 | -6.27765 | -59.92678 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bdf21ea-5b58-3857-9136-78ab7a292c03 | -6.57535 | -58.84243 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b98f0da-90ea-3b10-805c-b42d3f397c77 | -6.58151 | -58.84338 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70434dc3-a2fb-3b18-ae21-908cb596693e | -6.29007 | -59.93143 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc7614e2-9c94-3861-bf2b-cc98601e4af5 | -8.71571 | -62.56155 | 2026-09-14 06:14:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7312f9f0-6cf9-31c4-bc85-59bff6fd6e4c | -6.27823 | -59.92279 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 115e84b2-1b52-30de-b24b-39b5a22f1be7 | -6.13671 | -59.88528 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b379294-eb4a-3e5e-8f4a-33893967226a | -6.74255 | -59.43478 | 2026-09-14 06:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76d42b11-8bf7-3a1f-b8c7-815d182b3c0e | -6.27708 | -59.93078 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e11f75c7-59a2-3069-8b26-dc1c85113b79 | -6.31841 | -59.97978 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef83dcbf-ca9d-3c2f-84e9-7086f140aaf5 | -6.31031 | -59.95414 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17283c02-f638-355d-b20e-fdb8e5c86373 | -6.64044 | -58.82732 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11db32cc-e6ee-3cd8-ac43-adebcbf13a03 | -6.27918 | -59.92553 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d870e74-717f-3fa3-b434-686a0b5a9637 | -6.5864 | -58.85361 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 693c4b23-3c96-3a84-8627-6b132ee44244 | -6.58087 | -58.84809 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd9d177f-2823-3577-a0be-9c6c4b34e48e | -6.74316 | -59.43041 | 2026-09-14 06:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f44d794e-c219-371b-a928-298349358b79 | -6.28279 | -59.93171 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d5e7e26-a3da-3110-b49a-bed6c40a1617 | -6.59128 | -58.86386 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7886029-a974-3a6b-b691-9acf98b976ca | -6.79157 | -62.97682 | 2026-09-14 06:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de24b3b4-e01f-3eac-8df2-e856bd9fc50b | -6.27346 | -59.9246 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c804c7da-0f70-3045-acf4-9d052dd24139 | -6.58768 | -58.8443 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bef7cb6-f5f9-3f5b-b8b5-56844032cfc8 | -6.64112 | -58.82253 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 241d4904-a704-3baa-8b76-a2dc45165e92 | -6.31897 | -59.97578 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0127c28c-55be-3aad-8174-d081f267f250 | -6.29469 | -59.94037 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e640cde5-a4d1-3fec-b5c9-6daf6fead892 | -6.28842 | -59.94346 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a267238e-9c67-3467-bd83-5d6ccdb99328 | -6.31493 | -59.96291 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| da079e9f-7075-3317-aacc-67a6bd62d071 | -6.32252 | -59.99206 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 127fcd49-9b9d-3fd0-80e7-9d7aaa598301 | -6.68264 | -59.15476 | 2026-09-14 06:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9444b13c-1b27-3210-afc0-1aaad765d3d7 | -6.2838 | -59.93449 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 731a64b3-2b85-361f-a7ad-47553cac44fc | -6.32359 | -59.98444 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f0c19f7-4365-31bd-9309-9b58e258e8b1 | -6.58704 | -58.84895 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd283bab-c40a-3361-9755-00a4cd12fa6a | -6.59192 | -58.85918 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49c66ae6-9898-3c62-af66-54b17b9e2dd0 | -6.30976 | -59.95811 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9945e57a-ec91-3e49-bfa6-3599d2dc583f | -6.79088 | -62.98177 | 2026-09-14 06:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b116f931-9d0c-3bde-a4a4-12d6df25f3a7 | -6.58216 | -58.83868 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 590d7319-46f7-3262-aab6-e6239f098ac9 | -6.29253 | -59.95597 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70c4c30d-126e-314f-91ef-5794737f38fe | -6.28221 | -59.93573 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f31ff7f-0fb3-344d-98ad-cd5d355fe067 | -6.59809 | -58.86004 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81e1204f-57e2-3c3a-ae6a-464fee06c23a | -6.29524 | -59.9364 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7042003e-6f61-3d26-95ee-bdabe814bf8a | -6.79528 | -62.97562 | 2026-09-14 06:14:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1098038b-cd38-3285-9220-22b79fca0dd5 | -6.63969 | -58.8261 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e222d8bd-a4b0-364c-8023-d0818cde650b | -6.5747 | -58.84716 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c26f3553-6bfe-320e-b4ab-46d9c1343139 | -6.28395 | -59.92368 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7068dd6-22a9-3328-955d-8d4a56a4172e | -6.59322 | -58.84979 | 2026-09-14 06:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b35034f-bcb6-3fd4-822b-b34a0e5f6c2d | -6.28898 | -59.93939 | 2026-09-14 06:14:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0883a84a-0c84-354c-87e9-1da096977f30 | -2.88 | -50.4 | 2026-09-14 06:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30588b8c-c4b6-3fa2-a78d-6339c43b2ff4 | -2.91 | -50.4 | 2026-09-14 06:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b6dbf2b-3bf9-3449-9102-299777af9735 | -10.66 | -54.19 | 2026-09-14 06:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b53cd173-2106-3c11-b611-aa5d3581f4e0 | -10.69 | -54.13 | 2026-09-14 06:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4a7beb9-f460-3334-af7f-313216c00a40 | -2.91 | -50.45 | 2026-09-14 06:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cfdc03f-8532-3f9c-9fa2-126e264512c1 | -10.66 | -54.12 | 2026-09-14 06:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e33531cf-bfc4-3bd3-bb5d-4c3fd0d76c4a | -2.94 | -50.4 | 2026-09-14 06:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8120bf42-1875-39e9-80d2-4f6c663e85d6 | -10.69 | -54.2 | 2026-09-14 06:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efb734fc-7618-3b3f-a336-1ee78006feaa | -2.94 | -50.46 | 2026-09-14 06:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6865678-34d6-39f0-a8dc-2a4803632b21 | -10.6641 | -54.1491 | 2026-09-14 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 484.4 |
| 11ead1a8-59f9-3b45-b9b1-2f9cde0b1b65 | -10.6827 | -54.1679 | 2026-09-14 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 317.8 |
| 1eeb5a37-044e-3531-89a7-67551eea4746 | -10.6638 | -54.1696 | 2026-09-14 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 170.8 |
| 3a3277b9-6caa-3955-b24a-85f1f4604b3b | -10.6643 | -54.1286 | 2026-09-14 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 4e914d1a-0d26-30ad-93de-3f479265219e | -10.6829 | -54.1475 | 2026-09-14 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 735.2 |
| 949f250d-4c88-321e-8d8f-c2bb5408acbf | -10.6832 | -54.127 | 2026-09-14 06:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 556a7d58-7cb6-3b9e-8e82-c5187ad199d5 | -14.1861 | -47.3844 | 2026-09-14 06:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 91a05eb9-9577-3ca7-a527-2dedf0a1bcca | -15.5572 | -48.7953 | 2026-09-14 06:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 50dddef9-3e18-35e8-889d-b833226b1b4f | -15.5572 | -48.7953 | 2026-09-14 06:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 26e589f0-0b13-390b-80eb-b2836578b6ce | -10.6832 | -54.127 | 2026-09-14 06:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |


[Clique aqui para ver as próximas entradas](README63.md)
