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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 256a2211-f9f8-3d11-9334-f8db71d78dfb | -3.10448 | -50.36519 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eb993f7-e5fe-3eb0-a928-e7c3024d5547 | -1.82257 | -55.16712 | 2024-12-01 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 239dddf0-9954-305f-b821-c312b2a1d6f8 | -3.14184 | -45.37185 | 2024-12-01 05:08:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f64087d3-bd90-3d6c-bd2f-26093c4b362c | -2.83935 | -54.08749 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cd7c0e62-962f-3864-9e1b-ef2eec11a5a9 | -3.07188 | -54.56865 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3c28e9e-ee57-3b3d-82f5-247fcabcec86 | -2.88548 | -54.00637 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b874db34-f709-3755-ac0b-02498389c6e8 | -2.03381 | -53.50123 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ec47192-1bfe-3af9-874b-77fe472f36ca | -1.6586 | -53.42243 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa4ec28f-2cfb-306e-8981-5183f1510d65 | -3.2223 | -53.63095 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ce59034-48bf-3d1f-9a92-cbd962f73ecc | -2.78305 | -52.9949 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f7c209d-aabd-3d4c-bdc6-f1dfa44e6e9c | -1.24983 | -54.54782 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b65a57f5-441b-387a-bd51-4fe187eb10ea | -3.30675 | -53.83204 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98be11a1-808f-3600-9ebb-a946cda58af0 | -3.09209 | -53.72343 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33414429-707e-3c94-9408-6f3fd9db3ea3 | -1.4794 | -55.38633 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31fd21af-df09-3e9c-b843-a9a42356e97f | -0.53604 | -58.07954 | 2024-12-01 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ee9b5d5-d03e-3895-b124-b890de7e7ba5 | -1.69365 | -52.63658 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e54bc72-2f50-38d6-8830-bd43285f1b43 | -4.39931 | -50.69528 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1c07807-2dfe-302b-ad8f-83a19e06e6ae | -2.58612 | -54.24816 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aba235df-2829-3f19-8650-39c27fc0c7d9 | -2.8277 | -54.09358 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a4b57c7-544c-309f-ad8a-ae5708cbadba | -2.58788 | -53.98713 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4907e6d9-145e-3a73-98c3-93b1c9b73439 | -3.09325 | -53.28802 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7707986-0f3c-35fa-862c-d34290062ab5 | -2.92378 | -52.69102 | 2024-12-01 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfc1eb9f-77c9-3457-82fc-75fcd9ceef84 | -3.30219 | -50.03658 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5523ac00-9931-3238-95de-ae60491ee4fa | -3.06041 | -54.04775 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12772849-c14b-3fc0-a89c-6703ed33cdb5 | -1.92436 | -52.09642 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75b31186-732b-3578-b26e-2a42c5128337 | -1.89901 | -53.02352 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81c24861-0d73-30e2-9eba-8b07f5afcded | -3.09302 | -54.56797 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d98a7a8d-d880-3e72-9df9-238e8ed9bb85 | -2.53025 | -54.03699 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| adb195b2-4899-352f-8160-1716146064d8 | -2.306 | -57.08628 | 2024-12-01 05:08:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a2ddf98f-c6dc-3aa4-81f0-5261e562c7d0 | -2.63133 | -54.22335 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06db600e-49ff-3ae0-bffc-c49941245062 | -2.77441 | -55.33573 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdfc57da-be95-36b6-b5b6-d906b2328531 | -2.84915 | -54.10337 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3369abe4-695e-3eca-900b-f807b1ed13cc | -3.49536 | -53.80553 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4468511f-18ac-319d-9878-d157021d0568 | -1.82232 | -50.90311 | 2024-12-01 05:08:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5266c8d9-12d7-32b5-b568-30be08bdb4b5 | -2.85847 | -54.08907 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 536a377e-be24-32f3-92f6-de429bc33937 | -2.80922 | -54.07502 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4f0022f-a2d0-365c-83d0-1c651a42c0e9 | -2.62616 | -54.21099 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 012031fa-9740-3aa2-b1d6-ec7c224489d0 | -2.90237 | -51.57801 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ee414e6-ada6-3832-a677-43c93cd905bb | -3.46941 | -50.53417 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d960f3ce-ff24-3423-968d-2ef998770060 | -3.76762 | -50.17482 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6fbebc8-cd31-3824-96a1-15a6bb915f52 | -1.70122 | -52.43908 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23112b6f-ce25-3308-9564-27a256df4306 | -1.39902 | -53.39437 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66589220-3bf1-3c86-9936-7727908c7e46 | -3.05796 | -54.0561 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6625875b-16f5-3d41-b67b-aaaa23aad543 | -3.24616 | -53.91955 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9edfd052-b8eb-3870-84ce-7ea19e7941cd | -2.41338 | -53.66635 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27a0315a-f396-3827-8d53-4f997a1b04bf | -1.61342 | -52.35393 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a88e8d35-6bcb-33dd-9431-431a0b70d924 | -3.82357 | -52.24899 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e0599668-6f38-3571-8d91-03273f0abf6c | -3.15035 | -53.83661 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a863deb-1583-349c-a11f-a85eb74925da | -3.66192 | -51.72502 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8258a1f-94e2-3b8e-9798-a031d9337f2a | -4.19326 | -50.68844 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e00fdea3-c92d-3bb2-bed0-1e796a065951 | -2.38431 | -53.71424 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c0bf615-6d4c-3dd9-8bdf-29146ba4f019 | -3.11509 | -53.80718 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fba7e422-a18d-3c11-a8f1-4866a0055a4c | -3.6983 | -64.59351 | 2024-12-01 05:08:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f732895-d880-37ed-aa2e-09446c5c3bf5 | -3.01752 | -54.10912 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afaba3cb-50e5-30a8-a70a-cf6716681d18 | -1.49653 | -54.95461 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49f6f300-7ab9-35a8-9324-7b6cc4353e7e | -2.89298 | -55.2271 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55a2a67a-cad5-3585-85d0-7c58229707f9 | -3.10764 | -54.0431 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30a00847-c358-3c53-813c-39157e45bf79 | -3.59708 | -50.37715 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13f648f3-c699-33b0-a420-cae8d0e46785 | -1.44498 | -55.21654 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba823dce-030a-37da-bcf2-b4568fdfa7cc | -3.33573 | -54.06477 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf9d7c70-7f87-3d48-8552-8a57f069cd63 | -3.21608 | -54.22861 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b1c2f28-61bd-3476-ad93-5dd1c768fc6f | -2.36321 | -54.48447 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41345cd8-fe17-33d7-85eb-c2ef85ef2b13 | -3.27027 | -54.66688 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdbde361-c446-35b9-b72f-ed0cd72a1874 | -1.16246 | -53.77723 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 376103f3-ad65-3a28-8d94-ccafddc5822c | -2.58226 | -53.6737 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbb1854f-dd63-389d-9974-83fd46ffbee0 | -3.07496 | -53.80998 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17c4605c-1e86-3bb6-a9f8-18813a6493e6 | -3.25756 | -53.86913 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f72611f-4a81-30b1-9bec-a6e1f277d402 | -1.90762 | -52.87359 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8f6e702-18ff-3e8a-847c-33326c9d862d | -3.17877 | -54.33173 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a25237b-f6c8-3ad8-aa9b-e2ec383d29b7 | -3.02544 | -54.03528 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edbeff06-a871-35e3-976b-c4717306d431 | -2.80662 | -53.05832 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 686315ce-7cad-3286-91f3-88f7388ddf44 | -1.50638 | -52.56724 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8963f9a-f917-320e-ba11-d46a99e28d39 | -1.61034 | -53.82747 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94120868-b4e5-3a8a-8fc2-f7c02dc4c1ba | -2.96736 | -53.8952 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6194cd9-1b98-3c13-9764-cb75ea4a3eec | -1.56481 | -53.5147 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e11d5a57-470c-365d-98d7-ea8b59f29f15 | -5.65279 | -51.47123 | 2024-12-01 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba1dd16a-f1b5-3058-af48-3e63854fcac5 | -2.60247 | -54.25006 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 445fc96c-1b79-3fa9-86a4-20b091ee7435 | -3.13017 | -54.53183 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| b765dc34-7393-380c-a064-91af28e6195a | -2.77666 | -55.34328 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f47ebc94-89dc-3f6d-9955-7e4c6f1e5a82 | -3.02436 | -54.01925 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdf29501-a04d-379f-9d01-bd63809a38ea | -3.02894 | -54.03582 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c430657-f0e5-3b91-8808-3a7d0e387ae9 | -3.32298 | -50.19476 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44761f66-72c1-32ac-8014-6464db3cf556 | -4.55791 | -45.71529 | 2024-12-01 05:08:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b61f33b-8ab4-39f7-88c6-ed80d6369ee9 | -3.09944 | -53.27173 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8c1cae4-e0c3-3031-ba03-634000ccbeef | -2.98512 | -53.35795 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4daac2e7-e7bb-38df-b316-4ec282364b64 | -3.48288 | -53.81577 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3c470a7-0ff4-3447-9e6e-701fdeba2025 | -2.98577 | -53.28104 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bf5dbad-26bc-39f1-b5b7-76de40f50a7c | -3.06375 | -53.8123 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05addcd8-0aa7-3033-89d2-afaa08899768 | -3.17763 | -53.63643 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce60cf3e-b5d6-3154-8584-92b21d6c76a3 | -2.80362 | -53.05349 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a33bbaf6-a2c5-328c-a514-01a7572fcb12 | -2.45802 | -53.68142 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 463ebe89-b8a4-3090-9c4f-be8a1f9fa3e1 | -1.5417 | -55.94035 | 2024-12-01 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8d9fcd1-a89a-3359-aa30-ca9ac9cf6771 | -3.76956 | -51.6186 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 266677ec-990b-3f4f-8dd6-f70fbf3dc679 | -2.90008 | -51.58071 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81996018-fc01-39ec-92c5-95021e2f350b | -2.85812 | -53.99817 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d2554fd-dbd2-3f59-b607-74d24db401c8 | -5.10779 | -50.61539 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f8f8f2d-6014-321c-b85f-b09f0e32ad22 | -2.57498 | -51.88926 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d608b410-e672-348c-8ed7-07dbe991fb2d | -1.85403 | -55.61849 | 2024-12-01 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 371983fd-0a24-3f43-b009-d81156bb0c51 | -1.70405 | -52.64264 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e302e890-2421-3807-9f6b-2a64ae9fa8b4 | -4.06409 | -54.24583 | 2024-12-01 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README94.md)
