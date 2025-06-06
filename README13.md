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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 851b72f4-9094-3d8d-9ee2-25243c08c008 | -10.70211 | -57.64134 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 799579ce-e7ac-34f2-b83d-03ffdbaba5d5 | -13.71408 | -57.47852 | 2025-06-06 05:04:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 903009d0-3803-3466-9b48-72c1d8125616 | -10.30657 | -57.13923 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edae4ca8-45ea-3a41-bd16-25460dcf50b9 | -13.8827 | -54.67918 | 2025-06-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 860b2816-d777-3123-ab41-aebf7fc46482 | -10.30601 | -57.14273 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36807aa4-b31e-3e97-89a5-36379a90d49f | -10.33512 | -57.49435 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55e567bf-a07a-358c-bd33-f3c91424717c | -11.11933 | -54.66288 | 2025-06-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07ed26a4-3772-37f6-92dd-76ba827d64e5 | -12.95281 | -46.77261 | 2025-06-06 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5c30b81-3860-3a90-a009-eafb03042fcf | -10.94141 | -55.33157 | 2025-06-06 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbde7d3c-ad29-39af-b6ca-4f6177f7872c | -12.51967 | -58.35967 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9e7aab7-6b89-3ff1-afe9-a988edb1ae6a | -14.23421 | -45.48571 | 2025-06-06 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 411aca8d-ef17-30e0-84ed-b9073344aff9 | -12.83583 | -47.38254 | 2025-06-06 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 638937ca-ee7d-399c-80c6-c78e5ee07acf | -12.52552 | -57.24105 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09b9d023-5e74-361b-a733-44c546851e4e | -10.49411 | -53.65892 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6db4b62d-56ca-3144-bd80-08e0b7c49fdc | -14.02881 | -55.13311 | 2025-06-06 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d11826c-34a3-3268-bc24-2be8737dfae9 | -10.50189 | -53.65584 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af859aff-a2d5-38ea-acd2-33ff26afea26 | -12.83685 | -47.38148 | 2025-06-06 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddd65a74-cd7e-34bf-a30e-b06941d0bc61 | -10.29607 | -57.14112 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ec0dab3-9dcf-3bd6-8413-6bfe138d9f81 | -10.29663 | -57.13761 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd78ecf2-b368-37fa-a3fc-e1b1c2e15a52 | -15.08094 | -48.94458 | 2025-06-06 05:04:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c66cc900-3ad7-3ef3-a9b3-b886fb8304da | -9.52834 | -54.77185 | 2025-06-06 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80d9aff1-8ec1-3d11-b610-575fbf2eeff3 | -11.37421 | -56.55008 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af620766-5083-3265-bfec-8091a4be590d | -11.57874 | -54.89117 | 2025-06-06 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32ed9500-04a9-3467-b83a-6701a741805f | -11.37752 | -56.55061 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4067346a-3f54-35f0-bac9-fd2e6573c193 | -13.8833 | -54.67505 | 2025-06-06 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cc3b3107-1762-3ac3-95c2-d6a23c81799f | -14.04214 | -55.13916 | 2025-06-06 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d45513a5-30f4-3f29-b4cd-d5386802363a | -13.51451 | -56.5616 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f5fdeff-e4b4-3666-929d-4cd934ac580d | -10.66101 | -55.30753 | 2025-06-06 05:04:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36a17f77-e800-3591-8575-9323590d3345 | -12.66796 | -58.22113 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6d3f70e-ca7e-3241-9a15-08b568878254 | -10.69707 | -57.65145 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65b2279d-d367-3540-8767-fe0192c7f9d1 | -9.39724 | -48.42559 | 2025-06-06 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 519cba16-5faa-3ecb-917f-49ae52c318e8 | -12.96393 | -46.77782 | 2025-06-06 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 633b8613-73c8-33e5-8496-17789e97f693 | -11.3836 | -56.55518 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc8a43a7-d099-3024-952c-73ae0fffb781 | -11.13473 | -53.94585 | 2025-06-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 383b40fd-8352-3c91-b121-9c577fd6fb71 | -12.52221 | -57.2405 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 526907fc-0eb5-30fa-8645-a81204de8ca4 | -10.49551 | -53.66121 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 78941f51-70dd-3d92-ae5b-760acdef70e0 | -14.22458 | -45.49247 | 2025-06-06 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a98ed9d2-678c-36d3-9cc3-29fb02120733 | -11.13416 | -54.21825 | 2025-06-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d71d26dc-00f2-34b9-9099-1cc741655e3e | -10.46458 | -47.95192 | 2025-06-06 05:04:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 98cfe7b2-7ce8-3802-a360-25561f3b6301 | -9.66757 | -48.71467 | 2025-06-06 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b100e3e9-68df-331b-ba43-83fcbaf38f86 | -13.51506 | -56.55801 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0970fc4-b93c-33b9-8ae6-ee3ae67a8a57 | -10.46922 | -51.88993 | 2025-06-06 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a611258d-e0d6-3830-9a7b-40e7823a4906 | -15.00338 | -56.05248 | 2025-06-06 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b89b57a-de41-308e-92f8-96def8d5144e | -10.49193 | -53.66064 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e98f85b5-f958-300c-a228-bac43a6592a1 | -11.53204 | -56.45303 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b1b4bff-e61f-3399-87eb-5bd40a64bb6c | -10.30267 | -58.44277 | 2025-06-06 05:04:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4b9272d-f3ba-3c17-a8b3-21a5c7b5a6fe | -12.15669 | -43.20372 | 2025-06-06 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 655dd753-5ec3-329f-9361-723b05e05ba7 | -14.04273 | -55.13521 | 2025-06-06 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee612887-4442-3d10-ac87-9799b9324ba0 | -9.52437 | -54.77501 | 2025-06-06 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4da5248b-3b25-3dd6-bb6b-009a9e34997e | -12.66462 | -58.22056 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 361b2d9e-3b38-3e77-8a5b-7864a8712820 | -10.49614 | -53.65707 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 96c27a99-5915-32fb-ab06-402005d3a0e1 | -13.51839 | -56.55855 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 328632ba-3fce-3344-96ae-399fa2b4bc9c | -12.66128 | -58.22 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac334138-adc6-3ca3-9b4b-29003cbd0de7 | -12.52303 | -58.36023 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85fa2194-0e7b-32df-ad2d-32ff073dc509 | -12.95814 | -46.77719 | 2025-06-06 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13039b7a-51aa-3f67-b7b8-4f402e13c9bd | -11.37865 | -54.35072 | 2025-06-06 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0692af96-49d6-3844-85b5-274afd14976e | -14.22039 | -45.49461 | 2025-06-06 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57e4bc26-a237-3d64-a15e-679988a26b4e | -12.83593 | -47.38894 | 2025-06-06 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09f23e4e-0b62-3e9d-a2af-7712498dd2e1 | -10.47319 | -51.89049 | 2025-06-06 05:04:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b767958-017f-3481-a6ce-7fa45601a52e | -10.99323 | -59.1511 | 2025-06-06 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ceb5e03-d439-3a64-85df-617945fec679 | -13.07492 | -49.24661 | 2025-06-06 05:04:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faa7ffa2-f505-35ba-815d-55598a58556f | -11.07578 | -54.76989 | 2025-06-06 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ee14670-bd86-3b1e-a01e-6f3dfcd758a4 | -13.07562 | -49.24102 | 2025-06-06 05:04:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74d5aa47-847d-32d0-9980-acfa686e4458 | -13.52061 | -56.56627 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85122d5c-ee1d-3205-81ca-128dd43a516f | -10.33569 | -57.4908 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52ab719f-ecd5-3df0-86f1-8ed8d830c5cc | -9.20126 | -49.68995 | 2025-06-06 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64e075d4-7492-3b63-8fd7-95ec523d4101 | -11.37572 | -54.34624 | 2025-06-06 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f123cf7-a80d-38dc-b92c-5afb724fe416 | -14.74134 | -45.10097 | 2025-06-06 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dcea07b-1a7d-37a0-8d86-8c70649f72cd | -11.92231 | -54.81644 | 2025-06-06 05:04:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a8a3325d-35c6-352a-99dd-ea1d42f24ef1 | -13.51728 | -56.56573 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7dcd0bae-4352-377d-ab04-3809639bb7fb | -12.15595 | -43.21072 | 2025-06-06 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c48b8ab-91ba-3260-b6af-37675b7c399a | -12.53032 | -58.3577 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c4753c8b-668c-3060-bc0e-9434b6766544 | -14.22399 | -45.49768 | 2025-06-06 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcbb8ec6-f061-37d5-96b0-53195fca5c2d | -15.01019 | -56.05347 | 2025-06-06 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de8f3748-3613-3739-a843-5c0555113ef6 | -11.83724 | -58.8201 | 2025-06-06 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 137bdbc3-baaa-3bf6-a299-dbd2fc4bda2f | -11.53535 | -56.45357 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dae168d-40f9-32ad-9f82-af6b36fbecba | -11.13914 | -55.5258 | 2025-06-06 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abddcf31-1d44-3c87-b01c-34af835f7051 | -9.78865 | -63.39145 | 2025-06-06 05:04:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74a7e791-6213-3095-9206-2ff7b5e561d9 | -10.8082 | -55.87063 | 2025-06-06 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d5e8108-ec19-34b5-8067-973d34186e17 | -12.95235 | -46.77657 | 2025-06-06 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 95a1b0e6-8955-382b-bcdb-432c38b6a5e1 | -12.26783 | -55.07514 | 2025-06-06 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 958e3359-25ce-3efc-aeae-6a0e7757a8ed | -11.68761 | -54.55595 | 2025-06-06 05:04:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7cfe3bf-f2a1-3566-bb33-aa5feca6b5f9 | -11.14244 | -53.94288 | 2025-06-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09dccef6-4e89-3d8d-8520-057ca8c2a5fd | -9.84365 | -48.60732 | 2025-06-06 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14587e4b-ac4b-3cd2-8e78-2d69970c95c3 | -14.66627 | -53.1193 | 2025-06-06 05:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86cc459c-5790-3552-91c8-cc0cea56510d | -14.03925 | -55.1347 | 2025-06-06 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70adead3-2f98-3e0f-beda-426258df5a8a | -10.30328 | -58.43906 | 2025-06-06 05:04:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c861f1e-58dd-3b8e-aef8-b053ec66927e | -11.11588 | -54.66236 | 2025-06-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b65e362f-3237-397f-b50c-10c7f00e851e | -13.51617 | -56.57289 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a97c08cd-a51f-3028-9c9e-8ce7f4d41dba | -12.52697 | -58.35715 | 2025-06-06 05:04:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79ed3b91-f2b7-3efb-b98b-64dbba7c8148 | -10.69374 | -57.65089 | 2025-06-06 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 564c8759-eefb-334d-b737-b401b459d150 | -11.11242 | -54.66183 | 2025-06-06 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3f4e43f-8f2b-3576-81fb-212d58f0bc40 | -12.27127 | -55.07566 | 2025-06-06 05:04:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43be13ef-7694-3ea1-ba13-7e899ba70207 | -9.39874 | -48.42774 | 2025-06-06 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99a41603-12c0-38f9-b9a4-58d313e6ad06 | -11.53867 | -56.4541 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3172442a-db79-3b57-87ed-49e9408880e8 | -14.66555 | -53.12445 | 2025-06-06 05:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a882d2c-0655-3c4b-abc4-53c2fba6a3ec | -12.52723 | -57.18715 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d801aa3-058c-3811-bd8e-03ce92438d0e | -10.29939 | -57.14165 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4697e79-835a-36c4-b9b2-8ce97dbbdaf8 | -11.53092 | -56.43841 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1029e28-eb18-3015-bda3-7a9bd92493c4 | -11.5359 | -56.45005 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README14.md)
