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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e167a34f-5b51-3514-9d06-a009d6f329e2 | -12.02647 | -57.08606 | 2025-06-22 05:04:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 159d82d8-089a-32cb-bca7-a78a17701958 | -9.87422 | -61.39634 | 2025-06-22 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45b3614e-fc8d-30f4-b9bf-dd6a012be729 | -12.12994 | -58.18517 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a26504de-97ff-3c46-b475-ae4ef4b86027 | -10.52267 | -53.62049 | 2025-06-22 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 43402fae-0e7d-3c1e-b6a4-7be5b9a9b92e | -12.51182 | -58.34435 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30dc20fa-6965-3a18-be9f-14b4d0fdac87 | -11.84848 | -57.75772 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5613c7c5-3ac4-32e5-8dcb-d51a6fa867f9 | -12.57794 | -56.97015 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d0c9aca-0cf0-3ccc-b645-1a8e59bf3266 | -12.13444 | -58.17854 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9febc801-5e35-37f0-aee2-98947aae72a4 | -12.30489 | -50.08631 | 2025-06-22 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32cb7c4c-bd49-3f49-bcc8-814be9d89fe9 | -12.47314 | -54.42496 | 2025-06-22 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f549ee7f-8be4-3570-95b7-9b6e32424117 | -10.85986 | -53.76059 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbc2b335-7000-330d-99f3-35493e58eb10 | -14.02399 | -53.36798 | 2025-06-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 80c22494-d1ef-3a1b-b3cd-3fd6257a6208 | -13.14298 | -56.80752 | 2025-06-22 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f2b7fb2-891e-35b8-9b1f-d6f36ec4dee2 | -9.47654 | -57.82134 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb5c851c-cf82-37f8-8f15-38787aeb29df | -9.46634 | -57.84188 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7fe78e9-a9ae-37d1-a020-42e6f58666f5 | -11.74072 | -54.71556 | 2025-06-22 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 704d71f1-4287-3cbd-a08b-d1404242bbc4 | -11.10198 | -46.67939 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1398bbcd-b3c1-3298-a2d0-5f2cbafa9b04 | -10.92952 | -57.12714 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b587edf-15fb-3134-bbd4-79e417fb5812 | -11.61561 | -58.29224 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66550454-0bc7-3a98-8ce1-5f4a987752ad | -13.04427 | -53.70876 | 2025-06-22 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13bf0e67-7fce-3e5c-aede-7dc652ca22e5 | -9.10182 | -50.0252 | 2025-06-22 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bba45f2-1d51-3cfd-aa66-f388ed66f05e | -13.23809 | -48.41429 | 2025-06-22 05:04:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c107f8ba-87f2-3443-ae6b-4fa7bcd38c2c | -7.15725 | -55.4552 | 2025-06-22 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fe4d82e-d90e-3f36-857d-5c686a2af87f | -11.95221 | -58.76233 | 2025-06-22 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a52aafd-a914-346b-8c5f-ce73b9ae21fa | -10.86816 | -53.77867 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0028f093-0cf1-3d1b-a4df-e4d96193db54 | -11.14445 | -53.93521 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da9d4f25-966a-3dfb-b7b4-9b90d6159fa9 | -8.30902 | -55.09879 | 2025-06-22 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46393781-59b6-30e0-897a-b8a7e0eb91a3 | -12.47373 | -54.42092 | 2025-06-22 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d0640cd-b7d5-3509-88cb-eb6ecc9f15e4 | -11.53084 | -56.97705 | 2025-06-22 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80e94256-a6d8-3ef8-a583-7fa70659cce0 | -10.4453 | -47.02684 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99993034-1b3d-383f-8bc0-d0596cb23c5e | -10.22667 | -54.29732 | 2025-06-22 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8af079ca-5a27-36aa-ab43-0d4d402ac341 | -9.25132 | -57.52728 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6880197-2847-36db-a034-7d10eac9a3e6 | -9.92 | -59.9085 | 2025-06-22 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8270ae2e-f8c8-3d11-934d-7e01597ac84f | -10.52565 | -53.62522 | 2025-06-22 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d39b7693-75a6-373b-8009-7676b5db7ff2 | -12.50613 | -58.35826 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ade5bc8c-f028-3b01-a558-f768a3eca70c | -10.86704 | -53.76162 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5df921fb-06f2-3e31-82f6-41fa43a11ee4 | -10.43935 | -47.02952 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1eee1a8-3bb6-3d3b-bff0-a5b89a285ebf | -13.78712 | -54.29952 | 2025-06-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ca20268-130a-34eb-a48f-040a5f0bd031 | -12.51812 | -57.24166 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2450f36d-04c1-3cc7-8a4f-84e792cf7f04 | -11.57053 | -52.09343 | 2025-06-22 05:04:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4de3efb4-69de-3e8b-aa5e-6734b3eb0204 | -7.87423 | -47.88583 | 2025-06-22 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db2eddb1-46ae-340c-927c-f979516f39f8 | -12.02757 | -57.10065 | 2025-06-22 05:04:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ae15ef2-7dd9-3a91-970c-40957bebe9e6 | -7.87462 | -47.88293 | 2025-06-22 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 505d4130-7cea-3c40-8334-a47cd15bf837 | -10.9874 | -45.09389 | 2025-06-22 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f333d8e-3b4d-3584-98db-b6c2b11c8324 | -10.06395 | -49.66273 | 2025-06-22 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 93f8c56f-98d7-3137-acc5-fad70aa5f866 | -8.41594 | -48.30003 | 2025-06-22 05:04:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae273db2-d554-3636-9755-be4704929acd | -12.60814 | -48.37438 | 2025-06-22 05:04:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5311e18-64ee-3e54-9097-8eee6394619b | -8.60332 | -51.58439 | 2025-06-22 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9990e504-6f10-384c-9ac2-af54d4ec6857 | -10.86048 | -53.75644 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcb89cdf-daf6-3e2a-ae1e-0db517cd96de | -12.13386 | -58.18213 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ade3dd04-fb7c-3be4-9c07-2e4a65836dfa | -10.85925 | -53.76472 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75730143-dbe9-3aad-a4f9-1128591cd7a6 | -10.92677 | -57.1231 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9047611-ea4f-36ec-b6e6-66ea05499689 | -9.25858 | -57.5248 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfac7e3b-fe9e-330f-8246-32196d7855a4 | -10.92896 | -57.13065 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 150756b4-dde5-3915-b737-22ad6a4486e2 | -11.13618 | -53.91714 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb5e075b-cbb4-324b-a52a-277925db2da7 | -11.61285 | -58.28807 | 2025-06-22 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d45b7fb9-908a-3f1a-aae1-ad5e8fb01a36 | -8.4239 | -48.29914 | 2025-06-22 05:04:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0b824f4c-7eff-37b4-a60f-b8c83184848a | -10.5697 | -46.93106 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1bf5808-ceac-3fdf-b1e1-ebab3d82f720 | -11.11172 | -46.6641 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58557daa-bff2-3bc3-b16e-9164a67bf632 | -8.59484 | -51.59118 | 2025-06-22 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93d89110-ec6e-3e29-b2ac-8b2aac0458dc | -13.03998 | -48.84027 | 2025-06-22 05:04:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b9fc1d3-cdff-3875-83e8-ed90d905e7cf | -11.09898 | -46.67371 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4b3dc74-34db-383c-a606-28ec2b628b06 | -8.59954 | -51.58666 | 2025-06-22 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 04e24c40-a4c6-3358-aa1c-455aced3eba9 | -10.02697 | -54.32424 | 2025-06-22 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42d94a10-f480-3f7a-a267-8cdc4145692d | -8.59866 | -51.5889 | 2025-06-22 05:04:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8b0ab79f-a07f-365c-80c1-a91d5f4a585f | -13.6527 | -53.93796 | 2025-06-22 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aa93929d-b6f6-378e-ac66-e7733b897c6f | -9.4697 | -57.84244 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cf894dc-ac83-32fc-ba0c-953b8c84a213 | -11.42525 | -54.32947 | 2025-06-22 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f70f238-cd8f-33dc-9e57-37ada64baed9 | -13.79918 | -54.29257 | 2025-06-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6e46718d-f697-3857-8518-cfc18e93023d | -13.04503 | -48.84101 | 2025-06-22 05:04:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d831fa1b-06f4-3707-86e1-1c0451cf4ac9 | -11.10512 | -46.67084 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78acf715-55fb-3f7f-abef-073428ee4980 | -11.83738 | -57.76316 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd71637b-d915-3478-9909-b9c950fe9f73 | -10.86222 | -53.76937 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7af8dd71-69f5-3cb4-b606-cb55b45dd3cf | -13.29541 | -57.0938 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25010fe5-758c-32bd-99d6-487bb7d7ff49 | -10.16598 | -51.65426 | 2025-06-22 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbcc552f-478e-3a32-b8d4-bd6abef70ed4 | -8.12157 | -61.41423 | 2025-06-22 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7eb673bc-6723-377f-81d6-5fa5c2ee721d | -9.47086 | -57.83522 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee9c8b5f-016a-3824-9c85-f4b511de8e2b | -12.52143 | -57.2422 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7352ba09-cb67-3356-9282-53af504a8c9c | -11.13914 | -53.92183 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1310c170-88c7-3884-87de-771e7e35811b | -14.25237 | -45.50342 | 2025-06-22 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fdde456-1981-3352-9303-64ad3b6963c5 | -10.17947 | -59.51835 | 2025-06-22 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5919c82-525f-3525-a98c-d1629e8b3c4f | -9.25075 | -57.53085 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5df0511c-b550-3d99-a30e-15927708d9aa | -10.86642 | -53.76576 | 2025-06-22 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 166a9edb-6c34-34e3-92df-b7e550cdf4c3 | -8.45297 | -47.01146 | 2025-06-22 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03a0efe0-2b4a-31a6-9228-70073415b27b | -9.47318 | -57.8208 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d48b2975-fa27-30a7-a86e-b43a42e065fd | -12.51867 | -57.23814 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe58acb5-f6c1-39e8-a200-46d06e0ba7e1 | -9.46576 | -57.8455 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77bdcbcb-83e6-3d81-95c4-7da773e9eba6 | -9.25409 | -57.53139 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 271b98ce-193e-33ad-80a9-cb6c0f569609 | -12.47667 | -54.4255 | 2025-06-22 05:04:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 27685033-1422-37e5-8702-a4f841bcb8e9 | -10.98799 | -45.08883 | 2025-06-22 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9c34df0-1362-30e3-a645-51e9d31b5e02 | -10.03044 | -54.32476 | 2025-06-22 05:04:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34230374-68cc-38fc-b56b-07aca9b452be | -10.93394 | -57.12069 | 2025-06-22 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37186652-d214-3733-a41e-93655fdee330 | -11.10248 | -46.67544 | 2025-06-22 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef86ba9e-3b65-36a9-92e6-3332403eb34f | -12.5818 | -56.96716 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19f75206-20f8-3b12-8169-5cc540501cd1 | -13.26861 | -46.83315 | 2025-06-22 05:04:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7798e69-978b-3018-a049-6676b9d725fc | -13.79072 | -54.30006 | 2025-06-22 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4983507-0577-35c1-a245-765e83545c36 | -9.46069 | -56.05772 | 2025-06-22 05:04:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e880dea8-aead-387e-b5b7-8b40c3255b27 | -9.47306 | -57.84301 | 2025-06-22 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5ebce9e-a81b-3c74-9636-b26392a496c1 | -13.23802 | -49.83904 | 2025-06-22 05:04:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d71f8906-aba8-325a-ae3c-8296d74053a9 | -12.5242 | -57.22461 | 2025-06-22 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README13.md)
