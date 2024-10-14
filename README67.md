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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b23a0d73-3a81-3b3f-b3e5-d8d7e5519fc7 | -17.86039 | -57.38046 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 54be66ed-20f5-3357-8052-5a2a582f6e29 | -17.85961 | -57.38412 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 4d8c24da-6577-3ea5-85da-7b7119388725 | -17.85882 | -57.38781 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| afe8d271-fe7b-371f-9c1e-0ed819c0d7c9 | -17.85804 | -57.39148 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 56313b80-04ad-3c51-91a2-29e02ae7aa1f | -17.85726 | -57.39516 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 7de1ebd4-8c67-3a4a-8f9e-7db87fa76022 | -17.85653 | -57.37192 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| eb856a2c-5ee3-3843-816e-c304d282df3e | -17.85575 | -57.37558 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e3f2e0c9-9465-378b-b106-33ac10902d76 | -17.85263 | -57.39025 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9777fc1e-5011-332b-969e-0e768080bf12 | -17.85184 | -57.39393 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9300f0ef-35a5-3dcf-a1a4-ab32a0c615d8 | -17.84643 | -57.39269 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9131af0a-af4a-37d2-8c4b-5f82a6093b4f | -17.84565 | -57.39637 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 99f5ac33-5fb5-3445-a84b-eb7011b86cad | -18.26445 | -56.52156 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 01d5564f-7600-3dec-9c13-491f57444272 | -18.26379 | -56.52474 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 6c4820d4-b97c-3b85-b82e-3551a15d366d | -17.64601 | -56.29587 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3db032c4-4637-3370-8c6f-d260d8461f90 | -17.64536 | -56.29902 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 18ce32ae-ef9b-3f2b-84f8-96cba99f2c7a | -17.63962 | -56.30106 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cc724706-bd71-3b04-8a20-00f50c711d19 | -17.68863 | -56.24304 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 547cc109-f904-310c-9fdf-2a50ef9f1c33 | -17.67978 | -56.23463 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 5f7ba157-55e8-384f-8543-0542a6744114 | -17.64914 | -56.30643 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2b689842-ca57-3332-8cc0-bba02397f481 | -17.6447 | -56.30218 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 63b3127f-2591-323c-a8d5-62e82c675496 | -17.64157 | -56.29162 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d35ab9db-db58-3c4d-80fa-d9e36b7b3c69 | -17.64027 | -56.29792 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f6530fed-c1cd-385b-9d1e-06790e5be643 | -17.83044 | -57.30875 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 5141b1b1-3813-33f6-acc8-57a65a3ae0ec | -17.82965 | -57.31238 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 49c723c3-3771-33ba-a537-5d4a0e066de6 | -17.96609 | -57.31665 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 19378b9d-1013-3138-9151-5459a6b55a67 | -17.96532 | -57.32025 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 34247cda-d6e0-3834-9c00-c3f7ad3ffd39 | -17.96226 | -57.30818 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 22658eb8-59a5-30e8-8fd1-f7a3bc80480f | -17.96149 | -57.3118 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8a36e9b8-7537-3257-895b-1c3602798193 | -17.96111 | -57.30421 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 8a3537c6-d19e-30cb-ae66-108142590702 | -17.88893 | -57.29917 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 039cf244-a3b1-367b-90e6-e4c433ac3796 | -17.87894 | -57.29311 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.5 |
| 336a1f5c-36fb-33fd-9fce-9134947ed401 | -17.87356 | -57.29188 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 5b4e196c-f25e-3dfa-bf4c-9631e5bd85a8 | -17.87202 | -57.29915 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.7 |
| 68e474f7-15e9-332d-b876-0305c546733b | -17.87124 | -57.30279 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 64a8e895-d9c3-3ebd-81af-08d036655d49 | -17.87047 | -57.30642 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a683063b-49b0-3959-8b9f-d36c48409ec7 | -17.86203 | -57.29308 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| e3bcb993-1fa1-34f8-924d-ebb02918035b | -17.86126 | -57.2967 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| a9a6f3c6-8064-39f6-bc03-56497b5776a7 | -17.85587 | -57.2955 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| 3ee322bc-5606-31f6-a685-07583ecdb5b6 | -17.85273 | -57.30228 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 036ade7f-cd0a-3561-9a09-d5ae795bca2b | -17.84816 | -57.30515 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 2ba17319-0cef-38d0-b068-28852f741011 | -17.84809 | -57.29742 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 17b604c0-38ee-30a0-b19a-54d541be5b7a | -17.84271 | -57.2962 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 6dcec22d-3213-3b1a-a5de-c03abe98ca38 | -17.84196 | -57.29982 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 70a7c9cb-56ca-3006-8675-58addb07d371 | -17.84046 | -57.30706 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 03c96e04-a701-3abb-8350-e0e70839a471 | -17.83582 | -57.30222 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| ba88cb24-2c99-3d9c-aca2-3d0952a25a46 | -17.83507 | -57.30584 | 2024-10-14 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 30501a3e-c8f2-3ea8-8ee9-ec66132d5c9a | -22.88923 | -47.1356 | 2024-10-14 04:25:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a67ba040-807a-3ff3-a394-b61e2f5214dc | -22.54334 | -47.74422 | 2024-10-14 04:25:00 | NOAA-21 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df75042f-c92e-3830-9db2-acf7d2bc9257 | -22.58986 | -48.56478 | 2024-10-14 04:25:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 1e000361-9c9d-37a9-b382-3654cdee71cb | -22.58656 | -48.56417 | 2024-10-14 04:25:00 | NOAA-21 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 330715e0-45f5-3a46-b2ff-ff74fad7b292 | -28.5877 | -49.44121 | 2024-10-14 04:25:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| df094a22-b0d7-33e1-b73e-1a5d5d045128 | -28.58477 | -49.44182 | 2024-10-14 04:25:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d146d92a-68c5-3189-9d3f-1142804d55f5 | -22.29161 | -49.11291 | 2024-10-14 04:25:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3fea7d6-f675-30cf-ae89-b8a5fe7f6dca | -22.28166 | -49.11108 | 2024-10-14 04:25:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02098e69-1fbd-37cd-ae4f-ca8db4955058 | -22.27835 | -49.11046 | 2024-10-14 04:25:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79116059-a5d4-3b2d-9e01-d4ec825f2989 | -21.66243 | -48.96025 | 2024-10-14 04:25:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83dce3ba-4897-3f7f-ad9a-86982dc47764 | -22.36722 | -48.682 | 2024-10-14 04:25:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ed28d6e2-ba0f-3df2-8919-08bb6bb21524 | -21.87966 | -48.96469 | 2024-10-14 04:25:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f6b4e9ec-eff8-30b9-a3fc-8bb37d0852e0 | -21.87906 | -48.96842 | 2024-10-14 04:25:00 | NOAA-21 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f1ef741d-6ad7-3b27-9b99-a40be05cb03c | -21.64762 | -49.76167 | 2024-10-14 04:25:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 812d442e-f993-3839-80a2-7f05c1ed8c24 | -21.63426 | -49.84235 | 2024-10-14 04:25:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2316969a-b14c-3ba6-b523-03fbdb811157 | -22.54056 | -48.81215 | 2024-10-14 04:25:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10ffea1f-5335-3e40-b839-601749e18e86 | -24.24411 | -50.73804 | 2024-10-14 04:25:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 03b1cb3e-8cd9-3d54-9112-e99b4654f8ec | -2.4529 | -46.919 | 2024-10-14 04:25:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 54be587a-8b28-3080-8777-13e7e6dd5d3a | -2.6119 | -49.0772 | 2024-10-14 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| b72f7bbe-c4f6-3a4c-b800-e9aa7a06c225 | -2.6118 | -49.0985 | 2024-10-14 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 4a8a9299-1cd0-374c-a9c0-8fd919e08bf1 | -3.2889 | -42.8561 | 2024-10-14 04:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 41b63fbb-2c00-306e-8246-7d73fae0951a | -3.289 | -42.8327 | 2024-10-14 04:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 6a6f9c0a-f229-38dd-bf48-012d0139a2b9 | -3.3076 | -42.8553 | 2024-10-14 04:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 8c90aab0-587c-3448-bd98-b87349416c80 | -3.3077 | -42.8318 | 2024-10-14 04:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 223.5 |
| fd3b735d-09b2-3490-8bce-29586174e399 | -3.3078 | -42.8084 | 2024-10-14 04:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 705484b1-9bef-352c-9bbf-acb85bcff6e3 | -3.8383 | -55.9774 | 2024-10-14 04:25:28 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 3afc0e24-a421-35c8-a804-845fdae84463 | -4.1148 | -48.2515 | 2024-10-14 04:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 507b3c66-db99-3714-a9db-5cf653251865 | -4.1149 | -48.2299 | 2024-10-14 04:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 07926a8c-4dfa-3115-b79e-84c73be474d8 | -7.9418 | -63.6365 | 2024-10-14 04:25:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 0e3913c6-c1bf-324a-8f6f-7aedd98db363 | -7.9419 | -63.6177 | 2024-10-14 04:25:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| cb32742e-5389-3634-b5e6-1651b773e15a | -10.0615 | -44.2857 | 2024-10-14 04:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2361b913-ebb0-3a8b-97fe-da22002cf653 | -10.0619 | -44.2624 | 2024-10-14 04:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 298.4 |
| 3d90d697-b1c4-36f6-b798-bdf2e7044956 | -10.0622 | -44.2391 | 2024-10-14 04:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 1757a0c5-1aa6-308e-bcd4-a67efb553e5e | -10.0809 | -44.2599 | 2024-10-14 04:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 234.3 |
| 55e6f69b-e5ab-36b1-927f-a22d0c998c94 | -10.0813 | -44.2366 | 2024-10-14 04:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 153.5 |
| a2a4312a-838a-33da-81fe-cfa098439a13 | -12.3807 | -53.1167 | 2024-10-14 04:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1a1f5a00-3b7d-3908-a074-f6e20a5fcb3c | -12.3997 | -53.1147 | 2024-10-14 04:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 63c53e9c-c244-365d-ba2d-ae3de79af9f9 | -17.0004 | -57.4176 | 2024-10-14 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| acc9325c-0a58-310e-9f5a-0fca9b903387 | -17.0197 | -57.4358 | 2024-10-14 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 535bab05-b0db-3ac4-85db-a60811eeb2af | -17.02 | -57.4153 | 2024-10-14 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 7945dfb3-7226-3e56-8bb5-6e054318a851 | -17.1954 | -57.4767 | 2024-10-14 04:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| eb22d35f-4325-38d8-9701-be7a55b509ef | -17.1957 | -57.4562 | 2024-10-14 04:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 49bde14a-132f-3be1-ab5f-f9d779e34341 | -17.196 | -57.4357 | 2024-10-14 04:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| fd44586c-41ec-3f8a-a374-e15c2efe2f78 | -18.1902 | -56.8601 | 2024-10-14 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| b7c29930-4dc0-3ceb-a768-56d855f6161a | -18.1905 | -56.8394 | 2024-10-14 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| bda8934b-f572-364d-b4dc-2f6069c4290e | -18.214 | -56.6289 | 2024-10-14 04:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 5f77beca-b2ea-3cb6-88d0-598331531a46 | -18.21 | -56.8576 | 2024-10-14 04:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.8 |
| ed819a5e-247a-3140-85ed-939ca02eb236 | -18.2104 | -56.8368 | 2024-10-14 04:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 7cdacd19-2e42-31d3-9fc9-ed4b2fbee9d4 | -18.2144 | -56.6081 | 2024-10-14 04:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 175.2 |
| 664fa53d-ec6d-395d-97f3-bd3b6b69f475 | -18.2147 | -56.5873 | 2024-10-14 04:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 7cf2119c-87e2-30a4-92e3-91371f3345cf | -18.2338 | -56.6263 | 2024-10-14 04:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| af1f1baa-a09a-3ea1-90f5-e65f71ed9f81 | -18.2342 | -56.6055 | 2024-10-14 04:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 176.1 |
| 99139e8b-478e-3d56-ae81-05ab2ad695c3 | -18.2346 | -56.5847 | 2024-10-14 04:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 5234ec87-c333-3e4e-bf96-72336cb11971 | -30.13301 | -51.32142 | 2024-10-14 04:27:00 | NOAA-21 | GUAÍBA | RIO GRANDE DO SUL | Brasil | 4309308 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |


[Clique aqui para ver as próximas entradas](README68.md)
