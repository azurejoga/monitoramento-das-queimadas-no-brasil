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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57c4d36f-d0fe-3f5e-802c-273abfcdfa0e | -23.20067 | -49.63935 | 2025-09-18 04:19:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0765a909-fb90-3111-8fe9-2068458c84aa | -22.10755 | -51.21469 | 2025-09-18 04:19:00 | NOAA-20 | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ec219056-0278-3591-93e1-78d53880006b | -22.67128 | -47.45384 | 2025-09-18 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03169db8-71b2-339e-a58e-2673a78e6a3e | -22.33723 | -46.75682 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7c73f96b-f85b-3079-886f-c6eb448b8780 | -23.40232 | -47.42768 | 2025-09-18 04:19:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8499b385-fee8-3633-98ac-3c0be8041274 | -22.84965 | -55.10762 | 2025-09-18 04:19:00 | NOAA-20 | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| b13817c0-3a91-32de-97ad-ff7600685b4d | -22.65252 | -46.82373 | 2025-09-18 04:19:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5f76ae5b-5a4d-377f-9c89-b010280e5aaa | -22.24231 | -52.44626 | 2025-09-18 04:19:00 | NOAA-20 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2679ff49-6203-31ec-9bc7-6b01900b470d | -22.34892 | -46.74746 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 31a861eb-9818-35a9-8a17-491f92018837 | -23.46902 | -47.26607 | 2025-09-18 04:19:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 430c1efe-be73-3c9e-bb31-4b9caefc1b92 | -23.02261 | -47.08155 | 2025-09-18 04:19:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 29f196d9-8925-34a2-8796-aa0fda5a46ad | -23.46842 | -47.26982 | 2025-09-18 04:19:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 952bb967-8d15-3c98-827b-53f3b5178dd5 | -22.33392 | -46.75623 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cedd0b1c-09ef-3c72-ac8b-e264c14b35fb | -23.13856 | -49.64402 | 2025-09-18 04:19:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5d6377d3-0564-3b9b-b65d-76a1385dad48 | -22.96359 | -51.58444 | 2025-09-18 04:19:00 | NOAA-20 | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| be4f4c99-7bab-3c41-b8eb-8441d948413d | -23.1358 | -49.63922 | 2025-09-18 04:19:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3be0fa8d-fc66-3cb4-b5a2-68792581e5fb | -23.47941 | -46.43722 | 2025-09-18 04:19:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2f41d858-f07e-3dad-9abc-20bd5bb66b0f | -23.52109 | -47.26031 | 2025-09-18 04:19:00 | NOAA-20 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a7dd71e-f969-3b9f-8c6c-652ee96ef5d1 | -29.95186 | -51.61752 | 2025-09-18 04:19:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 08867fc2-165e-38ae-9518-b033b35ca109 | -22.5653 | -47.45738 | 2025-09-18 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5f78e893-ee7a-36fb-b953-4bd515de48db | -22.96171 | -51.59451 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| 9308edbe-b994-3c67-8f82-26393bceb9b6 | -23.13543 | -49.63597 | 2025-09-18 04:19:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8c6a75a4-8a20-36e9-b7aa-547c900e9700 | -22.67792 | -47.45509 | 2025-09-18 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc9f16e5-e7fd-319f-a4aa-3392bdd84dfa | -22.68063 | -47.45947 | 2025-09-18 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4849df74-0811-3459-bfc9-cc76af2fd17a | -24.04698 | -49.09076 | 2025-09-18 04:19:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bdf14a81-37db-37f5-ac8f-57a89d3d4f86 | -22.66856 | -47.44946 | 2025-09-18 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cd5ee2f6-81c4-3c17-86b8-cc9ff72cd9d3 | -23.34773 | -45.46904 | 2025-09-18 04:19:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 59c717ba-10a3-3c12-9b45-0ba67a13afdf | -22.84848 | -55.11309 | 2025-09-18 04:19:00 | NOAA-20 | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 104b6b7f-a684-308f-be9e-f10f1bc1747f | -22.06911 | -49.95951 | 2025-09-18 04:19:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 70a78dce-b95b-33e3-82ef-f0518e7752c0 | -22.08762 | -51.23674 | 2025-09-18 04:19:00 | NOAA-20 | INDIANA | SÃO PAULO | Brasil | 3520608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 36924011-8280-318b-85d6-010366284541 | -22.96741 | -51.58526 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| c251a7fc-593b-3929-b047-5cf3d8b26a3e | -22.96844 | -51.6011 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| b92e10c8-3791-3329-b49f-520bba6d4065 | -24.04359 | -49.09009 | 2025-09-18 04:19:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68b26c2e-2c11-33eb-a75e-edb0bc9ee6df | -22.09142 | -51.23752 | 2025-09-18 04:19:00 | NOAA-20 | INDIANA | SÃO PAULO | Brasil | 3520608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8b7b890e-1aef-31cd-b4d8-27bfe9561734 | -22.97227 | -51.60189 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 2b3283cc-f15f-3792-9e3a-f5fa49179e8a | -22.07343 | -49.95593 | 2025-09-18 04:19:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c82492d6-5b37-3324-84e9-e51ba9afe2e2 | -22.88802 | -49.97059 | 2025-09-18 04:19:00 | NOAA-20 | SALTO GRANDE | SÃO PAULO | Brasil | 3545407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dad1e33c-5d74-390b-8396-7a8befa28ddb | -22.08853 | -51.24025 | 2025-09-18 04:19:00 | NOAA-20 | INDIANA | SÃO PAULO | Brasil | 3520608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f847628e-bd10-34a5-87c2-949590615770 | -22.13304 | -51.18364 | 2025-09-18 04:19:00 | NOAA-20 | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a471fcf9-cb5c-3941-b1be-4d7f4ce32871 | -22.69571 | -47.53576 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c0b3b57d-63b1-3e47-9690-361df1d619fc | -22.65999 | -46.02819 | 2025-09-18 04:19:00 | NOAA-20 | CÓRREGO DO BOM JESUS | MINAS GERAIS | Brasil | 3119906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b11ea9bb-7ea8-3e26-b4ff-56f8abf42e17 | -22.46973 | -49.00647 | 2025-09-18 04:19:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b259c287-e003-34ce-bdf9-93e40b519036 | -22.34834 | -46.75118 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e400d127-8a35-359b-99c6-34b05a04bdcb | -23.09415 | -49.85369 | 2025-09-18 04:19:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d9b241ab-254e-33fe-8f28-cf99a145ff99 | -22.32846 | -46.74758 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 60d078a4-438f-34f4-a504-3e6e2840d671 | -23.13506 | -49.64342 | 2025-09-18 04:19:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b6f9bf78-5de7-3a72-9c3a-f4bab04f0907 | -23.97031 | -48.90043 | 2025-09-18 04:19:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11db9c74-2ca1-3120-93f7-1760eeaa3bcb | -22.67376 | -46.73164 | 2025-09-18 04:19:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 34c78990-c738-379f-9f8d-67fd85f60e69 | -23.77241 | -51.63596 | 2025-09-18 04:19:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 733c3069-3e55-30a4-9a2f-31b63f9c1d3a | -23.25726 | -46.73513 | 2025-09-18 04:19:00 | NOAA-20 | FRANCISCO MORATO | SÃO PAULO | Brasil | 3516309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 58b04ecc-8b90-363d-8a36-24fd3501fbbf | -23.09767 | -49.85438 | 2025-09-18 04:19:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c8ef793d-d5b3-3751-979c-dc46fbbefbe5 | -22.67045 | -46.73105 | 2025-09-18 04:19:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 72c8480a-6829-3c3b-8645-75f0394f684c | -23.13329 | -46.17504 | 2025-09-18 04:19:00 | NOAA-20 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5bcbe039-09ca-3d21-bcae-7991715ab30a | -22.34288 | -46.74254 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e94ae662-bf2d-3ff7-b4ae-fd80a9648b4c | -23.02101 | -47.99997 | 2025-09-18 04:19:00 | NOAA-20 | CONCHAS | SÃO PAULO | Brasil | 3512308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6cadf2df-14b6-3375-ba81-aabdc71ae9e6 | -23.43034 | -46.13604 | 2025-09-18 04:19:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 772f471a-ae56-315a-95f4-8e79ca010d15 | -23.77147 | -51.64091 | 2025-09-18 04:19:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| bde06fe3-2e9c-3e2f-8b96-ca771bde0338 | -28.28724 | -52.43645 | 2025-09-18 04:19:00 | NOAA-20 | PASSO FUNDO | RIO GRANDE DO SUL | Brasil | 4314100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2104ad6a-730f-33e2-8450-11aa8cab68dc | -21.56812 | -51.86528 | 2025-09-18 04:19:00 | NOAA-20 | PANORAMA | SÃO PAULO | Brasil | 3535408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| c021b140-cc21-3d1f-a9d0-51fcb845339b | -22.14155 | -51.18021 | 2025-09-18 04:19:00 | NOAA-20 | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c28750a7-96e1-3622-ac29-b4498153e01b | -22.84857 | -55.11193 | 2025-09-18 04:19:00 | NOAA-20 | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 52e72920-f8ef-3366-bd3f-0fac49cbe824 | -22.66341 | -47.50261 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d42cbdd5-14bb-35b3-8740-5cebd14a4406 | -23.427 | -46.13545 | 2025-09-18 04:19:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e748dbf6-5855-30a3-96bb-2e1eeae3c9bf | -22.3462 | -46.74314 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1cec45e5-37f0-3aa0-aed1-709a9e188715 | -24.04631 | -49.09474 | 2025-09-18 04:19:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78a4e55e-ef5d-3445-9175-7ff0201868fd | -22.6578 | -46.0201 | 2025-09-18 04:19:00 | NOAA-20 | CÓRREGO DO BOM JESUS | MINAS GERAIS | Brasil | 3119906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4d7f40d2-b136-3aa5-88fc-da7ae74e24b3 | -22.97321 | -51.59681 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 3b95ae6f-0a59-3aa4-8cb8-b2da397f9385 | -23.51719 | -47.26345 | 2025-09-18 04:19:00 | NOAA-20 | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 98029080-7b57-328c-9a5f-295516c93e0e | -22.6746 | -47.45447 | 2025-09-18 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3817eb8f-fa1e-321d-b436-94250d806095 | -22.34171 | -46.74998 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c24bdbaa-7eda-338c-8bd5-d0b037f69b91 | -22.47384 | -49.00313 | 2025-09-18 04:19:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ccfb4c8-d94d-3935-8fbd-711b57f6d173 | -22.69903 | -47.53639 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b10c45e4-e067-3678-bedc-cbf78347d606 | -21.57021 | -51.8543 | 2025-09-18 04:19:00 | NOAA-20 | PANORAMA | SÃO PAULO | Brasil | 3535408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 68a9cf14-a603-3795-b8ae-b061631c5d84 | -22.96264 | -51.58954 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 09d70087-7c62-3844-ae1c-fabd57612f2e | -23.13122 | -49.63951 | 2025-09-18 04:19:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 07a255dd-d2f5-300b-9529-4796c30b0b0a | -23.02039 | -48.00376 | 2025-09-18 04:19:00 | NOAA-20 | CONCHAS | SÃO PAULO | Brasil | 3512308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 71b14820-12d2-34fc-817b-a5db61a2de8d | -22.47727 | -49.00379 | 2025-09-18 04:19:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f014e48c-5b07-3aa1-b53b-e0a33c3b4747 | -22.12925 | -51.18288 | 2025-09-18 04:19:00 | NOAA-20 | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4b04ce39-a303-3003-a0cc-e03c09934ce8 | -23.89238 | -51.0344 | 2025-09-18 04:19:00 | NOAA-20 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1acbe438-5761-3938-a68d-50b305fed0c5 | -22.67609 | -47.50888 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3e795847-af67-370c-998b-67936614892d | -22.46905 | -49.01048 | 2025-09-18 04:19:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 586cdcf3-43e3-35d7-a50f-560a9cf6e2f2 | -23.1305 | -49.64374 | 2025-09-18 04:19:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2a335c50-bbbf-349b-82e7-361972c0886a | -21.56916 | -51.85979 | 2025-09-18 04:19:00 | NOAA-20 | PANORAMA | SÃO PAULO | Brasil | 3535408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 6cf161ac-d6dd-372d-bb5b-1592685d7215 | -22.70085 | -47.52514 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 268961ed-35fc-3346-86c2-5f19e97a3daf | -22.33749 | -50.16491 | 2025-09-18 04:19:00 | NOAA-20 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 7da47f50-bb18-3736-8202-8d31083cf744 | -22.69753 | -47.52451 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e745b4a7-0a33-3fb7-88ca-bab5a0781930 | -22.74002 | -47.44682 | 2025-09-18 04:19:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 97f992c6-37f5-3faa-a110-e1892c9ef4c4 | -22.56862 | -47.458 | 2025-09-18 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8016c9c9-ed41-3209-8bfe-edcb69a32f6c | -22.07267 | -49.96025 | 2025-09-18 04:19:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 2c2c0599-99f9-3616-8e8b-8ab6afc2e030 | -22.88017 | -42.98536 | 2025-09-18 04:19:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| eb8f4ac4-6006-3fe2-8de5-eb52fbefbe8d | -22.47316 | -49.00713 | 2025-09-18 04:19:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f86a4c8-e8cf-30ab-92cc-506b7bb55694 | -22.35107 | -46.75551 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e49bf2ce-3574-3b77-9fbb-c16b34006b60 | -23.0193 | -47.08093 | 2025-09-18 04:19:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 573139ec-38cb-3f7b-9754-ab719ffe41b5 | -24.04766 | -49.08677 | 2025-09-18 04:19:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9d4be764-895d-3036-b7cb-411b23caf4de | -24.04291 | -49.09406 | 2025-09-18 04:19:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e47e24b-3443-3b20-873f-62d7c175952f | -24.04971 | -49.0954 | 2025-09-18 04:19:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d223ece-30fd-331a-8be0-e4664d2d94ea | -23.14845 | -49.62882 | 2025-09-18 04:19:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 79413f57-1ccc-30b4-9e19-d3fd1c067252 | -22.65446 | -46.01949 | 2025-09-18 04:19:00 | NOAA-20 | CÓRREGO DO BOM JESUS | MINAS GERAIS | Brasil | 3119906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 330b3d39-72cb-35e0-9d9d-69bd4ba41080 | -22.06987 | -49.95519 | 2025-09-18 04:19:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2d9a7be5-6fe9-3295-a658-db52e153c35c | -22.96647 | -51.59029 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |


[Clique aqui para ver as próximas entradas](README28.md)
