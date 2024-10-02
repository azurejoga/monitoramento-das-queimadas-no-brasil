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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0833bed-6b1d-33a7-bb1f-bcd6a0f97285 | -11.35693 | -55.20358 | 2024-10-02 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e688390f-d0d8-346a-9213-c9cc0e3b5dff | -11.35567 | -55.19461 | 2024-10-02 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9e67a58-405e-39a1-9fe7-55bbb7d55848 | -11.3055 | -54.31763 | 2024-10-02 01:26:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e840f790-9cb1-3881-8721-d31c404a1bd6 | -11.30418 | -54.30841 | 2024-10-02 01:26:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f3e65a82-f98d-31c3-9d68-9697c58d0ecf | -11.23976 | -54.18287 | 2024-10-02 01:26:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 501b4c88-5f3e-3c8c-9466-8460d1439552 | -15.12491 | -55.83255 | 2024-10-02 01:26:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 7da3ab0f-bc80-3a31-be74-8c05ab8cd00a | -15.12362 | -55.82286 | 2024-10-02 01:26:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| c72457da-16ae-3f49-a2b3-35569078776b | -15.14175 | -55.82034 | 2024-10-02 01:26:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a451ca9f-3831-33bf-bfe0-d89fb76de7e5 | -15.13397 | -55.83118 | 2024-10-02 01:26:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ec20d03c-b10b-3543-b082-da3cc5b5b250 | -16.36661 | -55.97268 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9029e38a-b727-35a1-a116-539cafbbdb5b | -16.13711 | -55.42393 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 86c57b2b-7080-3c8c-a1c5-e9c5f864fdcd | -16.12684 | -55.41591 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7659868d-5e6a-338d-b39b-bb1e4b03c3c0 | -15.90428 | -55.40211 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 689aa5fc-a1fb-3c5f-9281-1463a8f5f26a | -15.51112 | -55.76254 | 2024-10-02 01:26:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3f89d95b-7f40-327d-9556-b9b1d367cc91 | -15.37356 | -55.83645 | 2024-10-02 01:26:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ec9d886d-0482-3c65-b1c5-dc161d368e0b | -16.64013 | -55.19754 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 44753772-6034-3fce-b452-4a9d0d62cf2d | -16.63242 | -55.20834 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3a392a68-e888-3f1e-8dfd-30a4cc578069 | -16.14534 | -55.41645 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 34b3f2cb-0f6d-3570-8717-75d9c22f63f4 | -16.13582 | -55.41444 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a60ecb36-4f08-3c50-a8af-7b1b1abbfe83 | -15.89527 | -55.40328 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9f260f5d-6b9e-386c-8a15-ec3b7bd74faf | -15.50984 | -55.75292 | 2024-10-02 01:26:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dfb8726e-adf6-3930-96c6-33992bb99c31 | -15.38393 | -55.84492 | 2024-10-02 01:26:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 161a8d71-4012-30ef-8fad-cd54e11a2c54 | -15.38265 | -55.83516 | 2024-10-02 01:26:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2339c622-55e7-3b84-ae2e-a7da140d998b | -15.37485 | -55.84623 | 2024-10-02 01:26:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 75bb465f-fb98-3dd3-917d-e1c604426b3c | -15.14431 | -55.83949 | 2024-10-02 01:26:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 2d0d3598-2ac7-351d-95dc-f0283c365760 | -15.14303 | -55.82988 | 2024-10-02 01:26:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78bc5b34-546d-32d8-985a-5c8302d3f71e | -15.13526 | -55.84085 | 2024-10-02 01:26:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0f7cb486-2766-3646-819c-f367ef4daa5f | -15.13268 | -55.82154 | 2024-10-02 01:26:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b1da7aa4-9d80-324b-8d6e-da2c4b453f4c | -17.20841 | -56.23367 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| 9d249728-7f1b-3e7f-8f9b-efc80f58b4a1 | -17.20707 | -56.22324 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 4e6e20e7-fd96-3c05-bc25-1ea8f5eece7c | -17.20169 | -56.25591 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| caf224d2-979a-3574-8465-6903879a569e | -17.19901 | -56.23502 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 25.5 |
| 59a6ee23-aa93-34dd-b133-ba1e8c4d9b5b | -17.19767 | -56.22458 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| a88fc79b-0323-3bb7-8ed6-5f9c44f4ba18 | -17.19628 | -56.28864 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| b8a738f3-86da-3975-9741-7cd082090e66 | -17.19495 | -56.27816 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 395eceff-8b7e-3d0a-8865-4144d1bfd3bd | -17.19367 | -56.19337 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| b34f9c76-3a18-36f7-82d3-b8a80b008011 | -17.18686 | -56.28999 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b9b317ea-b4d9-3b22-96bd-71885e08a117 | -17.18553 | -56.2795 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 8f7ed873-bda4-3de2-b96b-eed9c0ea4ca3 | -17.18296 | -56.18432 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| d9483ae5-4d25-3689-b7a2-de09766f7598 | -17.06485 | -56.70094 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 508a95a2-be48-3df4-b1b4-9216e6f441c6 | -17.16158 | -56.16626 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 0b66744d-1346-3e18-a8e1-8d3d34122ab8 | -17.16027 | -56.15592 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| f9234b2d-680d-3e40-85ba-a852836c372a | -17.15781 | -56.18312 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 73a40219-982e-3903-83b1-f34fbc181546 | -18.68897 | -57.32664 | 2024-10-02 01:26:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 4267f8de-d29f-3ed3-9651-abd0b9a975cf | -17.15645 | -56.17277 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 849b8d57-aeca-3aff-a639-5f4fa95b51c8 | -17.15509 | -56.16243 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.1 |
| 3603e1d8-fb38-3462-8691-f446983f2c8b | -17.15116 | -56.20519 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 26a4a3ab-51c6-39e8-b4f7-273dfa940135 | -17.14845 | -56.18444 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| d51873a0-6973-348d-a671-698384335b58 | -17.14709 | -56.17411 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| 89d19459-ca30-37cc-86bc-1f6281385f1d | -17.11895 | -56.40195 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 63ea0b64-9764-3e52-960b-efd6358d9e5f | -17.11761 | -56.39135 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 3f05ed42-f315-34c9-a484-c8ff9e49c7a3 | -17.11098 | -56.11624 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 4027788e-1d79-31cd-afc0-f34da615c726 | -17.10965 | -56.10596 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.5 |
| e1054543-2700-3337-807b-6627f58d5a64 | -17.10948 | -56.40328 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ee00da2d-8110-3d34-83db-429f63a9516a | -17.10831 | -56.0957 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| f3bb0573-469b-3759-80a0-bec6e043ab6e | -17.10032 | -56.10729 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| a78fb957-a0ca-3fd1-b887-c6b87e759b31 | -17.09099 | -56.10862 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| e88e616c-a53e-38e7-add8-6681e99ca900 | -17.08298 | -56.12023 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 60a36fe1-bad2-3b48-b8d5-3cdf8a472dd0 | -17.08166 | -56.10995 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 9e48b312-b6cf-3869-bdab-37fb01056669 | -17.07902 | -56.08944 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| e01076a9-6675-319d-88ab-f7fc11d5b18e | -17.07274 | -56.3826 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 9ca2f3c0-7437-3da6-8aa9-1e9e9573bb80 | -17.0697 | -56.09077 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 0d0cb3c4-81de-3aeb-98c1-16754286cf3f | -17.06837 | -56.20225 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a2b23c9c-f329-346e-a38b-236367622de5 | -17.06329 | -56.38394 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| ff36f97b-1766-3b86-aedd-90de219e3f86 | -17.06169 | -56.10235 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| c242d7c6-de31-35ec-96b9-4c259323f68a | -17.06038 | -56.0921 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| 3dcb803a-3d27-3816-81e0-6e2572943a39 | -17.05907 | -56.08185 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| a022bce7-943e-3b27-9af2-a760711ec7df | -17.05482 | -56.09929 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 06551006-aee0-3d74-be35-0d9cff8332ee | -17.05347 | -56.08905 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| b143b194-3313-3b6c-9cea-e9621a1e364a | -16.94955 | -56.21439 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 2bb9d4da-9364-3c73-b186-6be66b2b881b | -16.89122 | -55.8405 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 28.2 |
| 3da12182-4907-3820-83f5-7c2e36335308 | -16.88202 | -55.84183 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e1511695-96d9-3abf-8409-166da51c3828 | -16.88071 | -55.83187 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 7c4baeab-7b70-3194-97b6-7a17d2e02794 | -16.87282 | -55.84315 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| ced755a0-1755-34a4-a460-124e2ef15a68 | -16.86491 | -55.85444 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 32acbad3-3837-31cf-a0b4-bf7168eb40d4 | -16.86362 | -55.84448 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 27.4 |
| 13e9c884-f2c7-3fad-b60f-707438af380a | -16.86232 | -55.83452 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 5a7108b5-387a-3f9d-b0ee-d28f404acf2e | -16.85571 | -55.85578 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 83b9a942-8d2e-3e9e-905e-84aff6f559f5 | -16.85442 | -55.84581 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| f3c604f6-120b-3e8d-b9d4-4b6ec7515074 | -16.85183 | -55.8259 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| e68fe791-b17e-350f-9575-9b4d0dda018c | -16.80181 | -55.78873 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 57bce3e8-7890-3a53-918f-3c2c959d7c70 | -16.79263 | -55.79005 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 622bdbc9-9a00-31aa-9af7-79b8c3880cdd | -16.72526 | -55.49091 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e8c76f57-2d02-342f-bf29-f1d12451e18f | -16.70966 | -55.51284 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7805cd79-202b-30a1-9064-38ccc786dd4c | -16.70198 | -55.51993 | 2024-10-02 01:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 2ce523ef-92d2-3065-9d5f-eb4f919d7c9f | -17.10333 | -56.69561 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.4 |
| e1be6705-3111-3781-9331-a758980af666 | -17.10193 | -56.68467 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 95424a32-6c70-393e-b281-bd7a83ac405d | -17.0951 | -56.70789 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| c85a3478-b4d7-3111-bec3-3af290068ad0 | -17.09371 | -56.69695 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| f0101692-b9b8-3f2c-b9ee-60ec3a827081 | -17.08548 | -56.70921 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 8e216d9d-ab2b-3c58-aa4d-d493c418bbfe | -17.07585 | -56.71055 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 4fdf3e42-1f46-3b28-ad31-a83f8a5eda7e | -17.07447 | -56.69961 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.5 |
| ac587545-c00c-33d9-836d-6efb643fac36 | -17.05523 | -56.70228 | 2024-10-02 01:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| d7c3cc0f-73e7-3c47-bd0b-e43b91483c26 | -16.88456 | -55.9332 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 75509382-e823-3f81-ab57-5bc8f6f4f8f7 | -16.87402 | -55.92448 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 26.2 |
| 862b31d9-b326-3ed0-a805-a595eb950f38 | -16.87271 | -55.91445 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| 96abf7d1-baa6-331e-b2ac-a66de5d536b9 | -16.86479 | -55.92581 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| ce059ef1-7b80-3891-a8dd-ef662a4471bc | -16.86349 | -55.91578 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 54db5404-d086-3608-b422-ddb68a024f3b | -16.86089 | -55.89574 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 6f08f32c-b5bc-3137-a299-4a1eff0ed119 | -16.86073 | -55.96736 | 2024-10-02 01:26:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |


[Clique aqui para ver as próximas entradas](README35.md)
