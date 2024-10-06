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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fd1d6ff-fa63-3015-b853-a65796692407 | -12.6283 | -53.1108 | 2024-10-06 08:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2d743120-7c95-352d-beed-200b0f1bf1bf | -12.6532 | -54.0415 | 2024-10-06 08:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| ac88dd57-0aa4-35e8-9d8b-5a530f6f27ea | -12.6535 | -54.0208 | 2024-10-06 08:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 183.3 |
| 1d16dfd2-1b5c-3d95-ac2d-397f04c47be3 | -12.6726 | -54.0189 | 2024-10-06 08:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 4c4cec4d-0c5c-383b-9ba5-ce0459bd262c | -13.3786 | -61.9582 | 2024-10-06 08:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 91f3c5b5-6b5b-32b4-be04-cc8ed78e9307 | -13.3976 | -61.957 | 2024-10-06 08:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1b6e95dd-de1a-3dc2-9587-9627e8b437a3 | -16.3956 | -57.3845 | 2024-10-06 08:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 9e751d31-55dc-395e-8355-d6bb7f74e7e9 | -16.3959 | -57.3641 | 2024-10-06 08:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.6 |
| c253404a-da35-3151-bdef-7f58e499b458 | -17.0007 | -55.0607 | 2024-10-06 08:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 9903e3b5-1efc-3c1f-9fdf-4b43b57b7e76 | -17.02 | -55.0791 | 2024-10-06 08:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 51d931f9-03db-3a5d-8912-c443f9d5dd2a | -17.0203 | -55.0581 | 2024-10-06 08:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 689c4b3d-df76-3078-86c9-746123eba633 | -17.0207 | -55.0371 | 2024-10-06 08:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 7a1999f7-c685-340d-82b8-e7ebb9027c0a | -17.0985 | -57.4062 | 2024-10-06 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| e89ad133-5b66-38d7-a8a5-0e763c345170 | -17.0989 | -57.3857 | 2024-10-06 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 7c1b9291-077b-3e0e-9caa-cb0006588aec | -17.0992 | -57.3651 | 2024-10-06 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.3 |
| 2c7804f7-06e1-3212-a630-955d1293fd84 | -17.1182 | -57.4039 | 2024-10-06 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 28e5d655-1bc4-3718-9ecc-05604f97e121 | -17.1185 | -57.3834 | 2024-10-06 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.2 |
| 202cd0fe-3750-3e50-9265-4d0cf0dd6e8a | -17.1188 | -57.3628 | 2024-10-06 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 77772125-2f8d-35c8-8bc4-2727a5e35f2f | -17.812 | -53.7859 | 2024-10-06 08:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c4db44ec-30fe-3378-84da-b20dcf6d2886 | -18.6387 | -57.2785 | 2024-10-06 08:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.8 |
| 3ec2f23c-e460-3970-b595-ec07137c3cd2 | -18.6391 | -57.2578 | 2024-10-06 08:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.3 |
| f855944b-88a2-3bb7-a300-e51aab068dbb | -18.6586 | -57.2759 | 2024-10-06 08:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.0 |
| 4eb8a4d3-96ef-3197-85ed-5a5e26091690 | -18.659 | -57.2552 | 2024-10-06 08:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 148.0 |
| 2f62a408-7897-3280-8d8c-90b375dae4fd | -13.3786 | -61.9582 | 2024-10-06 08:46:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 13589947-6de5-323c-98fe-5f827c9aceca | -13.3976 | -61.957 | 2024-10-06 08:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| be0e9758-f084-388f-acce-eb5cd2ee8909 | -16.3956 | -57.3845 | 2024-10-06 08:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| bd6cb646-1255-3fcb-8ec0-826fdd98077e | -16.3959 | -57.3641 | 2024-10-06 08:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| a2fb2f3c-a872-3804-946b-a49e4e6951a8 | -16.5147 | -57.2486 | 2024-10-06 08:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 55042829-0476-3b3d-8914-ccb2bdae5f6c | -17.02 | -55.0791 | 2024-10-06 08:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 37926326-cf01-3042-a1d8-0140ced05896 | -17.0203 | -55.0581 | 2024-10-06 08:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 7afec4a3-2a50-3341-b3ce-6ed9b8d4e777 | -17.0989 | -57.3857 | 2024-10-06 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 62f3f03c-36c4-334c-8632-6134359f4477 | -17.1185 | -57.3834 | 2024-10-06 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.0 |
| 643f9f3b-659b-3f06-af0c-d2b66532c022 | -17.1188 | -57.3628 | 2024-10-06 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| a25c92c7-a959-3d8a-ae4b-c33ea15ef7cc | -18.6387 | -57.2785 | 2024-10-06 08:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.7 |
| 4cfcafb7-1347-343b-9302-0b0b7c8d2c98 | -18.6391 | -57.2578 | 2024-10-06 08:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 672e353d-02b4-31ca-a80e-20aa802659f6 | -18.6586 | -57.2759 | 2024-10-06 08:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.0 |
| eed92d6b-a4b5-372e-8625-f6c568ab365d | -18.659 | -57.2552 | 2024-10-06 08:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 137.8 |
| 73b90fb8-f4bf-37b5-b4b1-2d7a1b09e83c | -13.3786 | -61.9582 | 2024-10-06 08:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c08b96a9-3173-3872-89f1-8d0acc0020d0 | -13.8943 | -44.6058 | 2024-10-06 08:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| addd8f47-e4c2-308f-9af8-7cf671f6cc5f | -17.0989 | -57.3857 | 2024-10-06 08:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 3cf03b36-24ec-3901-ab78-7b0f62a5ceb5 | -17.1185 | -57.3834 | 2024-10-06 08:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.1 |
| bd7ed807-2c2c-3dad-a507-0e38e19be331 | -17.1188 | -57.3628 | 2024-10-06 08:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.2 |
| 8abce1da-0f19-367e-ae26-f8c5cad81976 | -10.42 | -50.69 | 2024-10-06 09:04:26 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e63931e1-ad5a-3971-a815-6630e8e34130 | -10.42 | -50.75 | 2024-10-06 09:04:26 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ca5e58cf-e76f-31e9-9090-16e0700e702f | -13.3786 | -61.9582 | 2024-10-06 09:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4340c05d-58f0-323a-bb4e-2ac2e85a363f | -13.3976 | -61.957 | 2024-10-06 09:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 38eeb78f-011b-379f-837c-fea89b67d6a6 | -13.3786 | -61.9582 | 2024-10-06 09:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0c35a9f3-b6dc-3368-a7f8-791e561cf758 | -13.3976 | -61.957 | 2024-10-06 09:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 6dde502e-d34f-36ea-bb29-a2109b289acb | -10.4427 | -50.7123 | 2024-10-06 09:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 183.0 |
| fd778894-cb63-307e-851e-d6ad5baa6643 | -10.443 | -50.691 | 2024-10-06 09:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 95278e69-8e36-387b-ae09-b1c444720ef6 | -10.4238 | -50.7142 | 2024-10-06 09:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 245.6 |
| dd2bcc0d-4d48-3a7b-988f-d2b9ce7cc25c | -10.4241 | -50.6929 | 2024-10-06 09:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 776d4871-0b18-33e7-8071-50fff4984bb9 | -17.02 | -55.0791 | 2024-10-06 09:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| f825b09d-f7e9-322e-81e5-be89e7e2d197 | -17.0203 | -55.0581 | 2024-10-06 09:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 283.4 |
| 1d7083a7-c404-358b-a17b-9d856974e48b | -20.4322 | -54.6978 | 2024-10-06 09:27:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 9a6d8062-2a9a-3a5b-9ea4-9b1e3f799f5f | -20.4327 | -54.6762 | 2024-10-06 09:27:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 150.0 |
| b31d3089-7af1-38bf-bebc-e88d8ac935e0 | -10.4241 | -50.6929 | 2024-10-06 09:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 9ba0f191-9ba0-3386-89fa-ac6f3342845a | -10.4238 | -50.7142 | 2024-10-06 09:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 4ac82d82-8649-3bb5-b95a-587b208c4011 | -10.443 | -50.691 | 2024-10-06 09:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 452a355a-d17c-3ae0-b284-dc7c83f740da | -10.4427 | -50.7123 | 2024-10-06 09:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 555c020a-edb7-3e38-939e-a0246ba898cc | -17.0007 | -55.0607 | 2024-10-06 09:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| a2845a43-c87c-3c4c-90fb-d4ba4887a652 | -17.0203 | -55.0581 | 2024-10-06 09:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 246.5 |
| 8786d107-85f7-3274-ba28-774cc1b4f33c | -17.0207 | -55.0371 | 2024-10-06 09:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 0dba52e8-8074-39f3-92be-f1d5c4c2ebdd | -17.02 | -55.0791 | 2024-10-06 09:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 26f1add0-27f4-35c7-8285-885e3c59a866 | -20.4322 | -54.6978 | 2024-10-06 09:37:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 103.1 |
| e20c6103-c645-39ef-ac31-dfb3bf133d63 | -20.4327 | -54.6762 | 2024-10-06 09:37:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 202eeb51-4611-3769-a49a-6b5b67953fa0 | -10.443 | -50.691 | 2024-10-06 09:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| a84a8c8e-03f7-3ad2-bccf-7b335b64acf6 | -10.4241 | -50.6929 | 2024-10-06 09:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| bfdd3ec2-ad84-3091-be3e-f68495381253 | -10.4238 | -50.7142 | 2024-10-06 09:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 251.3 |
| 693d602a-01d5-3ccc-87bd-6ef9e1c8e74c | -10.4427 | -50.7123 | 2024-10-06 09:46:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 8ada764a-a9e4-3e5d-8784-6c48b8805639 | -17.0203 | -55.0581 | 2024-10-06 09:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 312.8 |
| 8ed4585d-83cc-372c-a4ab-648b6cb4bba9 | -17.0207 | -55.0371 | 2024-10-06 09:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 8eed4630-4816-35d3-96ad-7ef4eaa038e2 | -17.02 | -55.0791 | 2024-10-06 09:46:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| c074ba41-4237-324b-b0ae-507a3dcfaf43 | -17.1185 | -57.3834 | 2024-10-06 09:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| d04b2e9b-3135-3d97-ba50-5fe9fadc82bf | -20.4327 | -54.6762 | 2024-10-06 09:47:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 143.8 |
| cec0e50b-78cf-3c4b-878f-c86bc4143bfe | -20.4322 | -54.6978 | 2024-10-06 09:47:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 7525ebb8-9bf3-3911-98c5-2b392ad25029 | -10.4238 | -50.7142 | 2024-10-06 09:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 233.1 |
| 6afcc61e-e65e-3370-8f4e-a9895aa3755d | -10.4427 | -50.7123 | 2024-10-06 09:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 155.0 |
| c7135b7a-2198-3e31-b2d6-8801a9fcce17 | -17.0007 | -55.0607 | 2024-10-06 09:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| a5e52c7f-a818-332f-b679-cf4229a5be02 | -17.02 | -55.0791 | 2024-10-06 09:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 7b25d5a3-952d-314d-b468-e2d14725f654 | -17.0203 | -55.0581 | 2024-10-06 09:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 264.4 |
| b368889d-21c3-329f-997e-dc2cd10b536e | -18.6391 | -57.2578 | 2024-10-06 09:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.9 |
| dd206fbd-8f07-3dda-9801-a2bd66917112 | -20.4327 | -54.6762 | 2024-10-06 09:57:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e7ac6ada-edd1-35df-9436-77349c0f3541 | -10.4238 | -50.7142 | 2024-10-06 10:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 239.1 |
| 725c7922-1aff-3a47-bc56-ec481af35ded | -10.4241 | -50.6929 | 2024-10-06 10:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 82a635a5-b657-3488-a5d0-1692d1d88e03 | -10.4427 | -50.7123 | 2024-10-06 10:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 5ca525f4-c8fc-33ac-8e06-5988b59e5fe3 | -17.02 | -55.0791 | 2024-10-06 10:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 4406b4e7-9586-300a-8d4e-c6fa3ed465aa | -17.0203 | -55.0581 | 2024-10-06 10:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 313.8 |
| 1d92dcbb-317b-30be-84b5-6c6a89b1f6ac | -17.1185 | -57.3834 | 2024-10-06 10:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 02e6c635-3704-32ed-a315-8fec032edcf5 | -20.4322 | -54.6978 | 2024-10-06 10:07:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 110.5 |
| cf7484bb-745d-33e6-9d56-0c07f8a699c0 | -20.4327 | -54.6762 | 2024-10-06 10:07:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 5a2234d4-1f66-34f8-9179-16273197fd69 | -10.4427 | -50.7123 | 2024-10-06 10:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 976ee9b1-edf5-306c-9026-a0bad463a395 | -10.4238 | -50.7142 | 2024-10-06 10:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 238.6 |
| 75346906-d128-335d-be29-fd5e6165d1e7 | -17.0203 | -55.0581 | 2024-10-06 10:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 279.8 |
| 7c796017-1e1d-3ee6-aa52-ee8422fed0a9 | -17.02 | -55.0791 | 2024-10-06 10:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 9afac0a9-0467-3802-a933-c5960d7674e4 | -17.1185 | -57.3834 | 2024-10-06 10:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.0 |
| 2cfc4fb0-0324-3138-9a92-37613ae45046 | -20.4327 | -54.6762 | 2024-10-06 10:17:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 2df611bf-3264-36f0-9709-2c57ee61ab2f | -20.4322 | -54.6978 | 2024-10-06 10:17:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 7cdbfbfc-a99c-330a-95e1-d2fe01de7f52 | -10.4427 | -50.7123 | 2024-10-06 10:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 9df937c1-6dc6-35e7-a53d-8898fbb71817 | -10.4241 | -50.6929 | 2024-10-06 10:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |


[Clique aqui para ver as próximas entradas](README159.md)
