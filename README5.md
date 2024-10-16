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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f65278d-b3e3-34af-bd78-8cb5e6904ae2 | -17.2013 | -57.3946 | 2024-10-16 00:39:30 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3c4a7e2-6362-39b2-8900-433106a42e1b | -17.205 | -57.416199 | 2024-10-16 00:39:30 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 19405d21-fb44-3508-92d4-b315672d5592 | -17.191601 | -57.3964 | 2024-10-16 00:39:30 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d78b86dc-e751-3b3f-aad8-83ebe4446282 | -17.189301 | -57.441299 | 2024-10-16 00:39:30 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33190697-2f11-30cd-a265-54c1b6bb8324 | -17.1931 | -57.463001 | 2024-10-16 00:39:30 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0b9fd1b0-6f2e-31e0-8b69-f0efeb904624 | -17.1796 | -57.4431 | 2024-10-16 00:39:30 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 86374931-759a-36da-bb69-ff48c77b05e1 | -17.183399 | -57.464802 | 2024-10-16 00:39:30 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7a1f1d2f-7d79-3549-baeb-1593dfbbefcc | -17.169901 | -57.444801 | 2024-10-16 00:39:30 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7dc63ae0-a5ec-3521-a1a5-24f30c710ccd | -17.1737 | -57.466499 | 2024-10-16 00:39:30 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1ee2830-5923-390d-b08f-2db6f4392a4e | -13.8965 | -42.502602 | 2024-10-16 00:39:32 | METOP-B | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 14311acc-fb56-37ce-bba2-68f00ab64706 | -16.964199 | -56.784901 | 2024-10-16 00:39:32 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2bce097d-23c3-3798-9fd1-19a64f4cb0bb | -17.0751 | -57.417702 | 2024-10-16 00:39:32 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2011648f-c850-3fb3-abbe-33e919c3a34e | -16.9545 | -56.786701 | 2024-10-16 00:39:32 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f5cbcdd3-8e68-3f6b-8a09-53c57efd19be | -17.0385 | -57.3801 | 2024-10-16 00:39:32 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f1a493c-724c-37e2-bc3d-cf984d26e1a0 | -17.028799 | -57.381901 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6eaa6be3-60a1-35ae-bffd-9d7e573bbaeb | -17.0326 | -57.403301 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b33dcd18-e12d-3ed8-8d8e-bc051f344266 | -17.0229 | -57.405102 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 115ac238-751e-3cc4-b3df-7f3743f615ef | -17.0266 | -57.426498 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3048c587-d125-36e4-8b30-1422753e26a4 | -17.013201 | -57.406898 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 054659c7-472e-35cf-b87e-ec6210cf925f | -17.016899 | -57.428299 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2aa6037e-6c13-33d5-b3fb-1adac3756ad3 | -17.020599 | -57.449799 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 05cc44ca-92c1-3d75-9c05-bf2eadfa44ff | -17.0035 | -57.4086 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 99b97732-adf6-39aa-8e0c-869d9a46f671 | -17.0072 | -57.430099 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bc0ab4ed-6566-3565-a0c2-51b61453c5dc | -17.0109 | -57.451599 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e72ec33f-1dc9-3eca-bfe2-9b056cfdc7c8 | -17.0147 | -57.473202 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8f50b454-c6d7-38a4-bc77-1728748af8e0 | -16.993799 | -57.4104 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 90932a2e-6e78-39c7-b83a-ac58f16b6a7b | -17.0012 | -57.4534 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 740b26e0-7d81-3625-89e9-5a9ee328ee7a | -17.004999 | -57.474998 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 393091e1-7684-384f-9285-03dfc71a52c8 | -16.9877 | -57.433601 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c13d5895-b7c4-3ee6-8d15-46e6e11bbe43 | -16.995199 | -57.4767 | 2024-10-16 00:39:33 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 10b9d5ab-0586-3e57-a1d9-f15e389b81ab | -16.978001 | -57.435398 | 2024-10-16 00:39:34 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c94b122-1d74-3bee-825a-34b0638cfc1d | -16.981701 | -57.456902 | 2024-10-16 00:39:34 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 80c0537b-b6c9-31f7-9177-27056b4edd15 | -16.9855 | -57.4785 | 2024-10-16 00:39:34 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a30df6f1-ad2c-3c71-9622-1e666062d23c | -16.957701 | -57.780399 | 2024-10-16 00:39:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f926daab-51de-3c71-864c-ce9aa4fb2b78 | -16.961599 | -57.803101 | 2024-10-16 00:39:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3db0ab58-0e57-333c-ac42-34b75d8e7378 | -16.9655 | -57.825901 | 2024-10-16 00:39:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b59500fc-6879-3678-a712-f701118020c6 | -16.948 | -57.782101 | 2024-10-16 00:39:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 13056873-9f5e-3ad1-9292-765a9e7dd98a | -16.9519 | -57.804798 | 2024-10-16 00:39:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 672dc4e5-ce1d-3750-ae32-3bfb2060c1d7 | -16.955799 | -57.827599 | 2024-10-16 00:39:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c4e395f-1146-3833-b923-7ab623126fe8 | -16.9422 | -57.806599 | 2024-10-16 00:39:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a20fa48-4d60-3f89-ae39-5ca29fa55a0f | -16.932501 | -57.808399 | 2024-10-16 00:39:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d91368a7-8669-3551-83f5-b150050b7e13 | -17.0051 | -58.2318 | 2024-10-16 00:39:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88e86fc0-56c1-328c-8178-f9ae3a5aa9ff | -17.0093 | -58.2561 | 2024-10-16 00:39:35 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 132114e4-6d99-319b-9c9b-8ca18bd0a264 | -16.9228 | -57.810101 | 2024-10-16 00:39:36 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84c35234-864e-3b0b-85f1-8e2a70ddeb29 | -16.999599 | -58.257801 | 2024-10-16 00:39:36 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 402359d3-942e-36e0-929e-f8a84d9c8fd4 | -16.909201 | -57.789101 | 2024-10-16 00:39:36 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1c141f06-6828-349c-8df4-d0caffba4e0a | -16.913099 | -57.811798 | 2024-10-16 00:39:36 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5209edac-f95b-3991-a0d1-3320850ff15f | -16.9034 | -57.813599 | 2024-10-16 00:39:36 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dee04d51-99e3-3857-80df-6c31693b0b04 | -13.56 | -42.730701 | 2024-10-16 00:39:39 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9a00bbc8-e2e3-3589-b5d1-57d98d8c4c7c | -13.5629 | -42.742599 | 2024-10-16 00:39:39 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9144f48f-4bb0-31a5-9dd2-b82867d203f6 | -13.5503 | -42.733299 | 2024-10-16 00:39:39 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 98e413c6-e4d2-36d6-a328-7941a38972c8 | -13.5532 | -42.745098 | 2024-10-16 00:39:39 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6ef73d75-6a19-38fe-af49-d59001f6d425 | -13.2482 | -41.935699 | 2024-10-16 00:39:40 | METOP-B | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 04359a80-7f5d-3adf-a895-d695fd2061cb | -13.2515 | -41.9492 | 2024-10-16 00:39:40 | METOP-B | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 998671c2-07d7-3d6f-ae7c-107ca62a64eb | -13.8159 | -46.935299 | 2024-10-16 00:39:51 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37f8d995-c54d-3f91-8383-75ef1bb16ccb | -13.3813 | -46.929699 | 2024-10-16 00:39:58 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5bb7ad24-17a0-3d5c-8d6b-f62aac02ef57 | -13.383 | -46.937099 | 2024-10-16 00:39:58 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f2f66a57-9003-36c9-bacb-3dc8eb4a5ed5 | -13.3847 | -46.9445 | 2024-10-16 00:39:58 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2ea221b6-7e8e-3a2a-9d37-f70478bca307 | -12.5282 | -46.809399 | 2024-10-16 00:40:11 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abef1510-43df-3f74-8900-03956ee78e3b | -12.4901 | -47.272999 | 2024-10-16 00:40:13 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5585f8d6-5170-3c50-96c4-d156c7734173 | -12.4917 | -47.2803 | 2024-10-16 00:40:13 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9774539-1d6b-37da-bf04-1d5beda21057 | -12.4803 | -47.275299 | 2024-10-16 00:40:13 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba300e19-ea68-3354-a7a2-4009006f2992 | -12.4819 | -47.2826 | 2024-10-16 00:40:13 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2b67902-87a2-3231-a4f3-18553d3fc998 | -12.5119 | -47.413898 | 2024-10-16 00:40:13 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c40438a3-68d8-3e76-a09a-4a58bfb5454f | -12.0468 | -46.6912 | 2024-10-16 00:40:18 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a2e49d2-a188-3855-82cf-ae9714d91e8a | -12.0485 | -46.698799 | 2024-10-16 00:40:18 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4f23da3-cd6a-3c76-89ce-8bf6dbfd9e92 | -12.0503 | -46.706501 | 2024-10-16 00:40:18 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 206f9ba2-3493-3598-ab3f-1899a143e100 | -12.3849 | -48.5863 | 2024-10-16 00:40:20 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47a2dc87-6f75-31b4-9508-e3aab5499ba1 | -12.3751 | -48.5886 | 2024-10-16 00:40:20 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46e66669-d87b-35f3-bd15-68e7558be1d3 | -12.069 | -48.372002 | 2024-10-16 00:40:24 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8451d506-3510-37ab-848c-eabf0b39344d | -12.0706 | -48.379002 | 2024-10-16 00:40:24 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d93fb71f-fa49-3c2a-8fa1-80e18c34d50c | -11.8855 | -47.6978 | 2024-10-16 00:40:25 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf5ad312-3e16-3deb-8e0b-076a2c82deb6 | -11.8872 | -47.705002 | 2024-10-16 00:40:25 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50508d36-f35e-3430-a63a-29fb44b32d32 | -11.7931 | -47.3829 | 2024-10-16 00:40:25 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e43a176-42ad-340c-88db-15ac943e95ca | -11.7948 | -47.390301 | 2024-10-16 00:40:25 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15af8bfe-c0f0-35e9-b399-8eff84517858 | -11.7965 | -47.397598 | 2024-10-16 00:40:25 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 994b4fca-b730-3013-b982-01fe2e476642 | -11.6185 | -47.206402 | 2024-10-16 00:40:27 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc94915b-9f24-3405-a861-65f3323dcd80 | -11.6202 | -47.213799 | 2024-10-16 00:40:27 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9724adc-6c9f-39a7-a494-5af025895889 | -11.6219 | -47.221199 | 2024-10-16 00:40:27 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04b87422-03f3-3519-88b3-bcbc7e175022 | -11.6404 | -47.572399 | 2024-10-16 00:40:28 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 039a250e-2201-30e9-83ad-45b66466d2e0 | -11.6306 | -47.574699 | 2024-10-16 00:40:28 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18b5e8e2-2594-3b4e-bd85-2961c8ed0414 | -11.6218 | -48.445599 | 2024-10-16 00:40:32 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 095a9e58-d7a6-3c78-9819-0f3e03170987 | -11.6022 | -48.4501 | 2024-10-16 00:40:32 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea46d606-5a2e-3b02-8c3b-7e01a4463330 | -12.0122 | -51.347599 | 2024-10-16 00:40:36 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3011f758-e9ac-38b8-84ec-e3fe76589824 | -12.0138 | -51.3554 | 2024-10-16 00:40:36 | METOP-B | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8ebb01d-3456-36ca-adb0-826b2fb33581 | -11.2066 | -47.8409 | 2024-10-16 00:40:36 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 147aa20b-b62c-31ba-b8d0-946e4573a11d | -10.9175 | -47.748798 | 2024-10-16 00:40:40 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83606b2b-06ae-3fe0-b5ae-418f036d6e9e | -10.7622 | -48.518101 | 2024-10-16 00:40:46 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57fcf5d8-85a8-3f45-8f9a-5e08a049e952 | -10.7524 | -48.520302 | 2024-10-16 00:40:46 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed29960a-39af-31b0-988c-5e3e767b3209 | -10.8302 | -49.234501 | 2024-10-16 00:40:47 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 940b5059-98cc-3592-8299-30c4d48aa852 | -10.8318 | -49.241501 | 2024-10-16 00:40:47 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c002e1b-da71-3589-b36e-40329fb4a766 | -10.8204 | -49.236698 | 2024-10-16 00:40:47 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 948e40ed-7bbb-3ee5-991a-4b0a271cd75c | -10.822 | -49.243698 | 2024-10-16 00:40:47 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00191917-6f15-3665-9e1a-1ebb847c5e4f | -10.2536 | -47.282501 | 2024-10-16 00:40:49 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa2be9e3-7518-3ed6-a4fe-fb73e8de4a9c | -10.2553 | -47.290001 | 2024-10-16 00:40:49 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb31f756-ab77-3548-877a-0bc72948e67c | -10.257 | -47.297501 | 2024-10-16 00:40:49 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65892fbe-eca6-3b0e-b6ae-39fd6cb354f6 | -10.2438 | -47.284801 | 2024-10-16 00:40:50 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbc5a9b0-9c42-37b1-a6f1-ad6cab200b20 | -10.2455 | -47.292301 | 2024-10-16 00:40:50 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1af50dbd-e267-3c62-b6d4-b4bdb8ee9dc8 | -9.9616 | -47.3587 | 2024-10-16 00:40:54 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 144e4207-4502-3bdd-a06c-f4b85fece35b | -9.9633 | -47.366199 | 2024-10-16 00:40:54 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
