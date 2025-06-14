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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d75cf4bf-024f-3679-83d2-faa3d03d787d | -10.9377 | -56.833801 | 2025-06-14 01:42:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac09e8c0-7665-3cad-85ff-97402a4a7245 | -14.2263 | -57.408901 | 2025-06-14 01:42:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed9e726-d9ca-3f69-8b66-3194c45cee7e | -13.9115 | -54.6283 | 2025-06-14 01:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00cd7499-070c-3255-b4c9-bad6bfb99205 | -13.9073 | -54.612202 | 2025-06-14 01:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ee743073-1e88-3afe-b421-d13b32bbf2d9 | -10.9474 | -56.831299 | 2025-06-14 01:42:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f55a37e5-dfe0-3feb-9ada-01a538e99f97 | -10.9409 | -56.8466 | 2025-06-14 01:42:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6baf45ca-7b99-3055-979a-c63b0865565b | -11.0257 | -55.103901 | 2025-06-14 01:42:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40e6a794-9815-32d3-bc03-c587b1a65233 | -21.447901 | -54.576698 | 2025-06-14 01:42:00 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0abb4b4c-9ff9-39e5-a1d1-bd57733daccf | -14.2166 | -57.4114 | 2025-06-14 01:42:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cad3369c-c77d-3152-9430-b4f1ac0aa6fb | -9.8828 | -61.4011 | 2025-06-14 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 809927b3-cbbe-3baa-bf96-6c77bc64b5e3 | -11.8201 | -57.345699 | 2025-06-14 01:42:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a30d326f-dd03-3a11-9adb-8229ee5fa289 | -10.9248 | -56.823502 | 2025-06-14 01:42:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8243e06-3088-33a0-985a-a044930d101e | -12.2887 | -57.275101 | 2025-06-14 01:42:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b19323ad-d0ca-3502-8739-444e892ecfac | -12.6287 | -57.896198 | 2025-06-14 01:42:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab58575b-8736-38d8-b479-c68fd0a20839 | -12.6236 | -57.875401 | 2025-06-14 01:42:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9cb8a51-3e1c-305c-995a-0eb552387e0d | -9.4772 | -57.860001 | 2025-06-14 01:42:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b05bde97-6800-3d38-a822-52ad93f29a3b | -10.9506 | -56.8442 | 2025-06-14 01:42:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f556db6f-d84a-3f06-85ee-545ec53f9e5b | -11.8133 | -57.359699 | 2025-06-14 01:42:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d8dfc34-3c47-34b5-bc33-f52db3ee27a6 | -10.9225 | -54.783798 | 2025-06-14 01:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46cf425a-6027-3d1f-a36e-90ef0933ab1e | -9.4744 | -57.8484 | 2025-06-14 01:42:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3961780-2d40-3cdc-8c5d-65d677f82704 | -11.0171 | -55.0704 | 2025-06-14 01:42:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53052907-0b18-3c62-9958-9ce40038dc18 | -13.9031 | -54.596001 | 2025-06-14 01:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ec89219-08c3-3455-8cb2-964a661d0e99 | -21.4447 | -54.5644 | 2025-06-14 01:42:00 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b7164510-1040-3933-afae-d7d57109fc6b | -10.928 | -56.8363 | 2025-06-14 01:42:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c298387-99cb-3c7a-b8ef-174b288ba494 | -12.6261 | -57.885799 | 2025-06-14 01:42:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e1c1bec-1f8e-3ed7-bb59-a0afd7a0eaa9 | -10.3018 | -60.548901 | 2025-06-14 01:42:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22a709ef-a297-32a4-a99d-45efce008844 | -9.8925 | -61.3988 | 2025-06-14 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14600ea2-b6ec-3c63-96f8-3f10c4a38a30 | -9.8845 | -61.4086 | 2025-06-14 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96cfb90e-6ced-3706-bc78-139a0c6d1353 | -9.3923 | -57.515301 | 2025-06-14 01:42:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa5de6ec-67b1-328a-896b-593bd2dc048b | -13.8976 | -54.614899 | 2025-06-14 01:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac232628-55fa-39d3-adc1-80828a678430 | -21.4543 | -54.561501 | 2025-06-14 01:42:00 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b834522b-66a1-3812-8f85-047630eb237f | -16.1537 | -60.081902 | 2025-06-14 01:42:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32330ddb-91b7-323d-a5a7-47e15cbb7b03 | -13.8934 | -54.598701 | 2025-06-14 01:42:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9841eb13-d271-3836-97de-df733aec8856 | -14.2237 | -57.3983 | 2025-06-14 01:42:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02344e12-ebef-3c3d-abf4-43ebb33982ad | -11.8104 | -57.348202 | 2025-06-14 01:42:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3428ea11-13f2-385a-8efc-76e3c9b7b8f3 | -9.4715 | -57.8368 | 2025-06-14 01:42:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a6a5975-ff45-3263-9fcb-12f7c3700397 | -10.9312 | -56.849098 | 2025-06-14 01:42:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b7aacb8-e37d-3ac8-8496-27323c66c3f1 | -11.8075 | -57.3367 | 2025-06-14 01:42:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7fde16d-8cb0-34df-a385-dcee5b3da840 | -11.0118 | -55.089699 | 2025-06-14 01:42:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e79b93f6-6e86-3965-b163-0265b91a9bfd | -10.3037 | -60.5569 | 2025-06-14 01:42:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9b825bb-8616-38ac-9fc6-edc61e3ac962 | -10.9355 | -56.8322 | 2025-06-14 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 0d88c351-8344-3f9b-b5b2-1f3cf8ff4dbe | -11.011 | -55.0967 | 2025-06-14 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 43c90088-e44e-36ca-bce3-4faabc1a6a9a | -7.2214 | -43.1153 | 2025-06-14 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 9f476b7d-c687-3884-88ae-c11fdfe8e704 | -14.2121 | -57.4098 | 2025-06-14 01:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 8b02e273-d89e-3d17-acae-748923737991 | -21.452 | -54.5675 | 2025-06-14 01:50:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 99.0 |
| ddbb1851-ee18-36e3-8304-60b16e06ab06 | -21.4315 | -54.5711 | 2025-06-14 01:50:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 5a8f7251-e8e2-30f9-a41d-6a565b0671e0 | -13.9062 | -54.6084 | 2025-06-14 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 28885901-32cf-329d-bcaa-daba20e6a648 | -6.9602 | -42.9052 | 2025-06-14 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 6c5804c5-224a-3ea6-ba54-feefe6385692 | -10.9353 | -56.8522 | 2025-06-14 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| bb62a0a1-4b6c-3c46-be12-57ecfcfcef96 | -13.887 | -54.6106 | 2025-06-14 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 2ab7b256-a6f4-3b93-bb65-f65e2fa76e8a | -10.9205 | -54.7795 | 2025-06-14 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 083ec256-8e71-318d-b7b0-139ad7a3ed9b | -11.0113 | -55.0764 | 2025-06-14 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e42ff32a-500c-3915-9330-d237e4c3be01 | -6.9605 | -42.8816 | 2025-06-14 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| d8cd9d58-cb3b-31fb-acf5-cdf9cc3d636a | -16.1967 | -46.4589 | 2025-06-14 01:50:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 54.9 |
| d9993fcb-7e3b-3c94-9e83-8d75e25bea89 | -16.1967 | -46.4589 | 2025-06-14 02:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 9f4bc391-183a-39e4-bb39-9f635bd0a131 | -6.9414 | -42.907 | 2025-06-14 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| c73d0777-5ac8-38c5-82b5-d843e1a18352 | -6.9605 | -42.8816 | 2025-06-14 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| db155d5b-6edb-3578-94b4-f1c999b092d8 | -10.9355 | -56.8322 | 2025-06-14 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d127c793-ea5a-3e50-9fca-9fe5e6d65f99 | -6.9602 | -42.9052 | 2025-06-14 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 8c5b6241-45c1-326e-9f75-9c424d55a0ac | -6.9416 | -42.8834 | 2025-06-14 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 8e5526bb-69f7-3fcd-9aa4-6d9e10177261 | -13.887 | -54.6106 | 2025-06-14 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 54c69cad-3916-3b63-96b0-a4249f0b4f8d | -10.9353 | -56.8522 | 2025-06-14 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 7426f227-a35f-3d24-abe4-388f3ca17644 | -10.9167 | -56.8336 | 2025-06-14 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 62721c39-a725-3226-9412-92d5d29e99e3 | -14.2121 | -57.4098 | 2025-06-14 02:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9ccb1494-e79f-37f5-ad08-375249be4b64 | -13.9062 | -54.6084 | 2025-06-14 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 913d6aa7-c83d-3651-b5c4-8cd702598df0 | -21.452 | -54.5675 | 2025-06-14 02:00:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 129fd5c1-8aff-354c-b121-2c25efab49dd | -7.2214 | -43.1153 | 2025-06-14 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 02ba0df3-0098-374f-ac3f-8ba1ac1315c4 | -21.4315 | -54.5711 | 2025-06-14 02:00:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d3c200d7-9276-3ef2-8b7f-e55e78d7c45a | -13.9062 | -54.6084 | 2025-06-14 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 31e5ed6d-b206-371e-b008-81b3030e1ad0 | -13.887 | -54.6106 | 2025-06-14 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 1d0b1cc7-8647-3a81-ba0e-ad6860cc21c9 | -16.1967 | -46.4589 | 2025-06-14 02:10:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 60.3 |
| d4e1ba04-42b2-35fc-a6f8-12d323ca49ab | -11.0113 | -55.0764 | 2025-06-14 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 1ed7b285-ddcf-32a4-9188-7337171e85e8 | -10.9353 | -56.8522 | 2025-06-14 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| fe9407b1-ebe5-3b7c-a551-21a30fb6350f | -21.452 | -54.5675 | 2025-06-14 02:10:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 070017d0-4185-35e2-9e8d-86e08c994934 | -10.9355 | -56.8322 | 2025-06-14 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 6597bbbc-845d-3b1e-b164-4750a572588d | -6.9605 | -42.8816 | 2025-06-14 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| 97fa2f7b-b589-3fe7-b00d-8666f582629e | -6.9602 | -42.9052 | 2025-06-14 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| d590be9c-61e9-3766-a6ff-2afbab01cf4e | -14.2121 | -57.4098 | 2025-06-14 02:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 9e6dd35c-b833-35fc-8be6-b41b0fb902c2 | -6.9602 | -42.9052 | 2025-06-14 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| ee07d15d-e06b-31ef-b066-1bcf19c0c408 | -13.887 | -54.6106 | 2025-06-14 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 1e783d7f-93ef-311e-aba4-7efb3f60d078 | -13.9062 | -54.6084 | 2025-06-14 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d1f0e524-1481-3f24-9b0f-307888dcf107 | -16.1967 | -46.4589 | 2025-06-14 02:20:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| e0e48cd0-99b0-30a6-b282-80f0f7ac5023 | -6.9605 | -42.8816 | 2025-06-14 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| c81271df-4e05-3d45-a314-976a712c1692 | -10.9353 | -56.8522 | 2025-06-14 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 87fc4305-7e07-3c0a-b38e-1c9597d3e831 | -14.2121 | -57.4098 | 2025-06-14 02:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 400325f7-2cbd-32c2-8f1a-11537ff45989 | -10.9355 | -56.8322 | 2025-06-14 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 3e4bde1b-b03c-3c78-b2de-2d240dd3bca8 | -6.9605 | -42.8816 | 2025-06-14 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| a196566c-2335-33e2-b222-00cad6789d5e | -6.9602 | -42.9052 | 2025-06-14 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 96092557-a71a-30ed-8adf-92659714b4bd | -14.2121 | -57.4098 | 2025-06-14 02:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b60f1a18-444b-3016-b2d8-d2155a7df6be | -13.9062 | -54.6084 | 2025-06-14 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0ac542ff-0fbc-3867-9592-3c354e00cf5c | -16.1967 | -46.4589 | 2025-06-14 02:30:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 8d47d5e9-099e-334f-b2de-401960f65a44 | -10.9355 | -56.8322 | 2025-06-14 02:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 450e3720-7a8f-3095-bec9-84dd0dc7d62d | -10.9353 | -56.8522 | 2025-06-14 02:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f52f8125-ae01-3ab1-a50e-1d4af5c1a23f | -10.9355 | -56.8322 | 2025-06-14 02:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 4d8b0dec-c4e3-3a40-b6da-9c625a7d8281 | -14.2121 | -57.4098 | 2025-06-14 02:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 32fbc330-cd62-3971-9c17-0ef75dfd150f | -13.9062 | -54.6084 | 2025-06-14 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 25a55a3a-1590-35f3-8c6d-9a1105bbc038 | -16.1967 | -46.4589 | 2025-06-14 02:40:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 39eb2ac1-5da2-3962-9f3c-30722f966da4 | -13.887 | -54.6106 | 2025-06-14 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 49511d4e-3e46-3239-8722-d5eade6db2e4 | -6.9605 | -42.8816 | 2025-06-14 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 967de99d-9ce8-3869-a884-bf8f0243839e | -6.9602 | -42.9052 | 2025-06-14 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |


[Clique aqui para ver as próximas entradas](README7.md)
