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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03483ed0-ec49-3d63-b8ca-1fbc0c890441 | -9.5126 | -60.53765 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec07aecb-d0a9-3b41-98a7-1d2807c4052e | -7.00784 | -59.83836 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29d0f6f6-00fb-39df-a81c-a19e51d8ffce | -8.99752 | -60.53201 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77b01347-03ed-331d-bef8-fd22d720971d | -9.55275 | -68.57518 | 2025-08-17 05:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0caa574-18e4-3c22-b74c-9e26e827fb36 | -8.88145 | -68.5136 | 2025-08-17 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e82d689-ee05-3605-a2aa-4d0238180bd4 | -9.04617 | -67.42147 | 2025-08-17 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0940ece6-aaac-3085-9109-fb8de05d027d | -7.53292 | -50.52566 | 2025-08-17 05:31:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e96de761-fa76-3127-a211-436dc4ebd38d | -13.01797 | -56.86239 | 2025-08-17 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e03d16f-7c03-3f3f-a375-3d6773f5c228 | -14.9622 | -54.76045 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d625e563-41e2-3af2-97c0-be88cb2c7562 | -14.93423 | -54.69033 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d3a6c3f0-e71c-3d86-888b-8c22ec837c81 | -13.424 | -57.02921 | 2025-08-17 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 965dc700-d6e4-3654-a4b8-60fb3e3b9f5f | -14.92853 | -54.69263 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0cb9583e-8ab6-36c1-9649-16d9e8c9fa7c | -14.92394 | -54.68569 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1840eb3-0652-3281-ad45-8f4e55418634 | -14.97356 | -54.75552 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f090ffb3-7213-313b-94c3-d156eb9024b9 | -14.93459 | -54.6873 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6595a7e3-b120-37a0-9cb4-15cefea1a4d4 | -14.95727 | -54.75644 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8aab9473-83c6-3a35-92bc-a1dcdd4fcc80 | -14.63334 | -54.89382 | 2025-08-17 05:33:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e768da79-2986-3cdc-9dc3-7ac6b70978b2 | -14.70946 | -59.66324 | 2025-08-17 05:33:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eca8595b-e6da-3e18-a91f-ee1d05c170ac | -14.98512 | -54.74896 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c6480762-a080-36bf-bf02-6fbc2dd50462 | -16.62824 | -51.36665 | 2025-08-17 05:33:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 664b8f64-c178-3346-8dbe-6f802cc70806 | -15.18336 | -53.83722 | 2025-08-17 05:33:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be2f9a70-43ca-3797-8985-ceb8d6de01b2 | -14.55526 | -52.03468 | 2025-08-17 05:33:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9eec5e00-321a-330f-875e-5a07bc2e7e7d | -14.96256 | -54.75729 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e21c3490-f9a1-3d27-8671-40f9f2810323 | -14.84069 | -59.63606 | 2025-08-17 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cba0c149-4740-3e9b-a804-9ee7bf72a8a3 | -14.98017 | -54.74507 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 423a50ed-8b89-3fa6-b050-9676516757dd | -14.9569 | -54.7596 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 87246fca-76f8-352e-995f-d4186bbcc286 | -14.96716 | -54.76422 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b32bad19-b1ec-345d-a5b7-36b674f38ba0 | -13.43293 | -57.03044 | 2025-08-17 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2390eed5-de8d-3500-bca6-12a783aba4fc | -14.97983 | -54.74804 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f727f73-d936-33b9-b17b-9d2fc2e601d9 | -15.85811 | -50.20329 | 2025-08-17 05:33:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db9bd42e-646c-317f-b2ba-4f6936df5e40 | -14.9795 | -54.75085 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a398703e-c810-37b4-b7e2-8cc61bf9268a | -14.54896 | -52.03395 | 2025-08-17 05:33:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3d8cfbab-2c64-3161-a26e-9a310b4fa869 | -14.80394 | -59.58997 | 2025-08-17 05:33:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cc2200d-d605-3210-bfca-3dd86481bd12 | -15.18902 | -53.83795 | 2025-08-17 05:33:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c28159e-3e11-3cc0-b09c-1a7e5d0f7197 | -14.96861 | -54.75165 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1024d58-24dc-3bc6-a106-ece6f387010e | -14.84386 | -59.64142 | 2025-08-17 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d579399-9af9-31dc-99a5-532800b54f68 | -14.98476 | -54.75204 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 45346e21-a564-3d41-9924-2173fa996f4f | -14.91977 | -54.67522 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38ecebf4-de3e-36a5-9d91-fed5cbf07635 | -14.93386 | -54.69342 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 273bb79e-2df1-3eb8-933a-49523908e3d0 | -14.84174 | -59.63794 | 2025-08-17 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52e97b9e-48cc-3fa1-b365-25beaa4b25f2 | -14.84001 | -59.6409 | 2025-08-17 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2293e4a6-481d-3e6a-9e30-91ebeb4b3e92 | -12.78947 | -60.15524 | 2025-08-17 05:33:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d3a0fd5a-92d1-36ff-9502-1508a0c08e37 | -14.9739 | -54.75256 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9c7d01ba-2510-3ae0-b6f1-839b343df668 | -14.98441 | -54.75505 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 279b0815-0360-3e6b-b678-14210085c179 | -15.85578 | -50.19353 | 2025-08-17 05:33:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f20a35bf-04a9-345c-9843-ee1db3d5e246 | -15.85884 | -50.19584 | 2025-08-17 05:33:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f78c54ec-1117-3988-ac36-0cc851f856f2 | -14.96753 | -54.76104 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ae54b6a-1af7-3486-8bf5-cdb331fe805a | -14.97424 | -54.74971 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| aff4620b-ede7-3985-b226-f4467dd2b6ab | -14.91939 | -54.67843 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e4a0b03-547a-3761-977c-8a335cafb09d | -16.62768 | -51.37247 | 2025-08-17 05:33:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5104e897-44b5-362f-bfb7-55482f5b1721 | -14.92468 | -54.67949 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a409987b-ac1e-3aaf-bdf4-4a5ef4deb9cb | -14.70564 | -59.66259 | 2025-08-17 05:33:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0fa879b8-6329-3802-9fcd-bc562951d42b | -13.42847 | -57.02979 | 2025-08-17 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a886d56-83a2-3b5b-9bd6-a39d908ba520 | -15.8551 | -50.20089 | 2025-08-17 05:33:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5326e3d0-9f78-30c9-bac7-371649d0a3a2 | -14.92432 | -54.68257 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6d19728-405d-3573-914c-1fcfe5f58c0f | -14.92505 | -54.67638 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e728fa6-6fc5-36cc-8f6e-70d6d4a16501 | -15.86219 | -50.20195 | 2025-08-17 05:33:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc9279e3-63a3-3b56-add4-66098f268219 | -12.78885 | -60.15953 | 2025-08-17 05:33:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0b73303a-dcd1-368e-95f0-99069bafd4f2 | -14.96826 | -54.75472 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50dbfd0d-6ff6-3396-bd64-f0533c7b64a2 | -13.14171 | -57.17502 | 2025-08-17 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32b35962-5f44-3d62-a83b-bb766c92aecd | -14.95197 | -54.7556 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44922faa-0591-3975-8a60-7dfa2e9d798b | -14.97918 | -54.75364 | 2025-08-17 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5ada1fc9-c7b0-3319-9eb1-2e997b18fc21 | -22.17466 | -56.11422 | 2025-08-17 05:36:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82b5a0ea-f1ec-3173-8e06-3d4dff8b1791 | -22.17433 | -56.1176 | 2025-08-17 05:36:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9845ec42-16c2-31f6-a869-86eb1e4be059 | -22.2132 | -56.19875 | 2025-08-17 05:36:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 740182d4-5331-32d8-bd05-ed5aac0f459f | -22.16934 | -56.11352 | 2025-08-17 05:36:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a9c949c4-7bf9-3d29-8479-d3ecfabeec9f | -22.16899 | -56.11702 | 2025-08-17 05:36:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd5085e8-21d5-3c26-9b93-4c1eb2c0396f | -22.21286 | -56.20224 | 2025-08-17 05:36:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f10f9d68-5e76-3f19-b22b-6b50f294a82d | -14.9819 | -54.7536 | 2025-08-17 05:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| fc29743f-6f61-3b30-9bed-d137d20b89a4 | -8.9788 | -60.4964 | 2025-08-17 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ce88fc51-f845-36e0-bf78-0c4682ef8feb | -7.62111 | -44.96401 | 2025-08-17 05:42:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ecfa9164-11c9-3690-ab3a-9a55765e0269 | -3.97711 | -42.52681 | 2025-08-17 05:42:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 13d29f48-b4d7-3791-b019-3d7944ded3d7 | -7.1442 | -44.629 | 2025-08-17 05:42:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 872f7fdc-f4b7-31f4-8807-fe5cd89899a0 | -4.60103 | -43.30213 | 2025-08-17 05:42:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c812635f-de5b-383c-b428-cc3c789d9c5f | -6.18959 | -45.4417 | 2025-08-17 05:42:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 806adc63-aa53-3fa4-b4ac-ac31c5ea7e74 | -4.91997 | -43.25988 | 2025-08-17 05:42:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 334bc47a-d817-379b-8d8d-88383b941c68 | -8.50753 | -44.72693 | 2025-08-17 05:42:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f6f40607-7aa3-3cfd-89d6-2f3844b2cd2d | -4.92129 | -43.25106 | 2025-08-17 05:42:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 8e9eb30a-8ac6-381c-980f-11fb028becb2 | -6.54532 | -43.01815 | 2025-08-17 05:42:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 639c3647-8c32-33e7-9c6a-9614bb19a253 | -4.91248 | -43.24978 | 2025-08-17 05:42:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 645d04ef-1715-35bd-880b-bbaac2892471 | -6.182 | -45.43106 | 2025-08-17 05:42:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 018034dc-d3a3-378b-bbb1-dd77350d0dd6 | -7.14287 | -44.63781 | 2025-08-17 05:42:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| eb4d3300-7d87-3f90-802c-d6d581256952 | -7.14154 | -44.64665 | 2025-08-17 05:42:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9330e8ec-7909-34fe-81a1-dc8f7eb3b145 | -4.59841 | -43.31969 | 2025-08-17 05:42:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b223ed6-330f-3026-9f42-d6cdbc1f79d0 | -3.97844 | -42.5178 | 2025-08-17 05:42:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 1cbb122f-bd31-36bb-9419-0cf8e3d60874 | -8.5062 | -44.73576 | 2025-08-17 05:42:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5e324f7f-ca12-3052-91a0-4a47237dd1ff | -4.05309 | -46.92925 | 2025-08-17 05:42:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 473fe24e-8a60-3832-8ff6-1e251d765049 | -6.18059 | -45.44029 | 2025-08-17 05:42:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 35c6f0c1-c2ea-3f13-aeb5-fe7a482d128a | -6.6109 | -43.87715 | 2025-08-17 05:42:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 873f1a89-c617-39b1-8a7d-48a932f8b6a8 | -8.03448 | -47.66587 | 2025-08-17 05:42:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cbc83fe9-7ce9-3c49-8b55-ce5b73f9d2b3 | -8.49742 | -44.73444 | 2025-08-17 05:42:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| acc29306-ff89-35f0-b919-bfe0266b9d99 | -6.54397 | -43.02724 | 2025-08-17 05:42:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 76a75fbf-5028-32db-bb1e-64c22ec5f789 | -7.62246 | -44.9551 | 2025-08-17 05:42:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b2a64a2b-5506-3f14-908a-d233d02c2d49 | -13.60232 | -46.89751 | 2025-08-17 05:44:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 689309d9-22da-381f-bcab-456c6fa8b3f2 | -13.58449 | -47.78208 | 2025-08-17 05:44:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 7cf6f752-57fd-360f-b90e-880387faba0b | -12.61124 | -46.91114 | 2025-08-17 05:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1cc6441c-255d-3606-b24a-a92d9a0e1e53 | -14.97131 | -54.7542 | 2025-08-17 05:44:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 3b7498e7-6e8f-3ad8-9b85-1e3ee3582277 | -13.56972 | -46.98842 | 2025-08-17 05:44:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f9880ecb-2d97-3e22-8789-94d000661f40 | -15.18346 | -48.77058 | 2025-08-17 05:44:00 | AQUA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5ff34239-9510-348a-ae62-b86606efe33c | -15.85288 | -50.19453 | 2025-08-17 05:44:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |


[Clique aqui para ver as próximas entradas](README37.md)
