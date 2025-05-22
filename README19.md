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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f119a3a2-4756-3d8b-bcc9-0c68eb93f086 | -13.44507 | -47.55009 | 2025-05-22 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9699eea7-c7df-3b88-a9f3-56256518ef6c | -12.66717 | -58.21647 | 2025-05-22 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55185410-a785-3472-9e21-26d5c5d7fd3d | -14.01941 | -55.13806 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 52803d47-3fac-32f3-8ff2-7ac31fbae719 | -12.29503 | -52.50109 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a39a7e97-7cd8-3a9c-a778-cdab4fa0b8b2 | -12.3396 | -49.97039 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88e24f65-e4b6-34a6-afe5-04b670ea79ce | -14.01441 | -55.12508 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd177231-4693-39e0-8dbb-3d3feb3c4463 | -12.29779 | -52.50515 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 71e8b07a-ee9b-3dcc-b563-725272959907 | -16.28497 | -58.66969 | 2025-05-22 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ff23f82d-8f99-3ab3-89ae-fd467c354ea2 | -12.35444 | -49.9758 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb775791-fcb9-3548-b5f6-4aa74f7e311e | -14.03561 | -55.13627 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 734ad844-f534-3963-a860-d6337946b7cb | -15.08011 | -48.94342 | 2025-05-22 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 433de246-dd25-3274-a24c-7befe1cd8028 | -13.67158 | -53.94191 | 2025-05-22 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a14af751-e532-384a-8623-98c63ba91411 | -12.48489 | -57.18693 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6152ea88-f242-305b-b1ec-8d5be8ada527 | -12.27595 | -57.26934 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 71f99483-6528-3494-bd73-b5a51a9efe9c | -12.48883 | -57.18766 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fda0a4d-699a-3d77-8787-a5bb8647c653 | -18.13633 | -52.05564 | 2025-05-22 04:46:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e574ec2-892b-3779-a845-f258b903e2b2 | -11.64483 | -58.26361 | 2025-05-22 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a416b9d-4917-3d7b-8006-d0336229c59c | -12.33439 | -49.9576 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0205ae2c-5d09-301c-b3be-8f6bfd494cb0 | -12.34826 | -49.98379 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f0d1c2a-2d14-3e4b-9e18-2e32457c77a0 | -12.13003 | -54.65945 | 2025-05-22 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a6b6f27-cc7a-3fc8-92dd-9a94a31e7b76 | -12.72034 | -54.97098 | 2025-05-22 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4546494d-581d-3776-b5f2-4ed1de175bbd | -14.02288 | -55.13866 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 822c21b7-8413-3d4c-b9a2-9a74e4add485 | -14.04923 | -56.05937 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8160c009-3db4-3fad-95e8-9731053eba9d | -10.9894 | -59.15821 | 2025-05-22 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86534b0e-00dc-31a8-806c-ec580439edad | -10.82817 | -56.96064 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 08c18c57-0704-3852-adaa-f69370750dbf | -12.6868 | -58.13152 | 2025-05-22 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c036ca13-6d28-343f-9055-05d80fcaad3a | -13.80132 | -53.30115 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 47ca774c-ddc1-3a4d-866c-41ad19f9a0fe | -11.85868 | -52.27487 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 32c6b323-b1d1-33a4-b871-0c34dfc96fdb | -19.1603 | -47.81831 | 2025-05-22 04:46:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 330d5617-03a7-3813-ab75-06af6b1ebe4c | -13.80203 | -52.89302 | 2025-05-22 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 115186ac-3ea3-3725-9315-b268609253fb | -12.12115 | -54.66996 | 2025-05-22 04:46:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e2e7b6b-9361-31e2-8b10-043540d8b4a3 | -16.68192 | -43.88294 | 2025-05-22 04:46:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51b743ac-80c8-3090-a759-bc4abf98f807 | -10.68332 | -57.59101 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36e3785d-c621-30a8-a4f7-ed0f273f816e | -12.49877 | -57.21706 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f84d995c-0e0a-3025-b1b8-1c1d0e6faa8d | -13.51401 | -43.69542 | 2025-05-22 04:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2357a1f-bc24-3f2f-b2c2-230256b7dd36 | -12.02652 | -63.79141 | 2025-05-22 04:46:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78bfee35-3d75-3710-a919-db263777eb8e | -13.7135 | -57.48399 | 2025-05-22 04:46:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fed73afc-cab0-32c8-9196-ce41a622a59d | -17.55677 | -50.52681 | 2025-05-22 04:46:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23b8fa5f-a9df-3d68-9a1c-c7f438bf4da3 | -10.68195 | -57.5987 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6370658b-805c-330b-b946-550a07fea0a6 | -10.82018 | -56.95932 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63135230-c9fb-3fad-ac4c-02e84ad7b09d | -12.28785 | -52.50353 | 2025-05-22 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c4faa84-fb2d-39e4-ad41-3a2b867c788a | -10.68059 | -57.60631 | 2025-05-22 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e04f8260-aae3-38f3-8c99-7fc86eaa9c74 | -12.34308 | -49.97093 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0e6ea6a-95b2-327b-b33b-57b6f71cd861 | -12.50363 | -57.21262 | 2025-05-22 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4ab78a7-29ea-3d6f-9545-d6bd37ab09f7 | -12.34367 | -49.96702 | 2025-05-22 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a38b731a-224f-3b12-898c-74b418f1a0fc | -17.70654 | -47.49524 | 2025-05-22 04:46:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1067fe8-e361-39f3-aff9-f5ba1a0a7ade | -17.83685 | -50.81111 | 2025-05-22 04:46:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8946403f-1b17-3e16-b9bc-e246301c6c9a | -13.78019 | -54.3122 | 2025-05-22 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fad4415-d8ab-30cb-bbb0-667171abcab7 | -14.01376 | -55.12898 | 2025-05-22 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8415544d-7131-3bcd-82fd-e6b5c99d5346 | -12.42053 | -54.36313 | 2025-05-22 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f75b76f-68ae-3395-8025-dbdc17a492a4 | -11.06771 | -55.07639 | 2025-05-22 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5105a107-d984-323c-afdf-c6e36a4e335d | -21.21834 | -48.60865 | 2025-05-22 04:49:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d6e0ba6a-97de-3acc-9fd3-1ecb4577cf5d | -20.99619 | -51.79168 | 2025-05-22 04:49:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9eaa0f8b-58f5-3b34-b4fc-dc810f9c4f23 | -20.15166 | -54.22718 | 2025-05-22 04:49:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 87f59ded-ccbb-370e-974a-01f8d1b66c74 | -20.95857 | -48.63135 | 2025-05-22 04:49:00 | NOAA-20 | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8f282c3c-7861-32c6-be12-60be8af87daa | -20.94755 | -56.59453 | 2025-05-22 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 53bb8fb0-4850-3d2f-86e0-6c77b39e03b1 | -20.61944 | -56.08112 | 2025-05-22 04:49:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2738887-7746-32f5-9aee-aa6267fc4c7f | -22.16217 | -42.93849 | 2025-05-22 04:49:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5af74f1e-e97d-3e8f-b926-dcff4320f244 | -19.7332 | -54.50833 | 2025-05-22 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91d019ea-416d-3f85-b6d4-7aa83feecc46 | -23.29288 | -51.58825 | 2025-05-22 04:49:00 | NOAA-20 | SABÁUDIA | PARANÁ | Brasil | 4122701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 995e5559-5d0b-31a9-93de-c33d32ac738e | -22.14736 | -56.12589 | 2025-05-22 04:49:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bed750a0-0052-3641-b8c5-d63495799d7e | -19.05387 | -53.45362 | 2025-05-22 04:49:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e7ee9c35-7c7f-38c4-b9f1-58fbd1870498 | -20.47814 | -53.67457 | 2025-05-22 04:49:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fca2d051-031a-3e55-96b7-b447f55db1df | -20.32623 | -54.23867 | 2025-05-22 04:49:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7057f22e-5308-38d3-bf21-31c026cd8d71 | -21.5336 | -49.52909 | 2025-05-22 04:49:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9dbc94cb-fbd0-3857-b1a2-c1b1428ee229 | -21.46538 | -56.29536 | 2025-05-22 04:49:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b764934-5051-32ca-b457-dd4b45b9bc9c | -20.60839 | -48.8643 | 2025-05-22 04:49:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 02f199ae-0f5d-3ac8-a997-f1d10b859d47 | -22.16289 | -42.94007 | 2025-05-22 04:49:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| fdb6d47f-5ae1-3733-b71b-f2d5e1a33b31 | -20.52474 | -56.80124 | 2025-05-22 04:49:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63b32c8f-ddcf-36fb-8466-6ee3fe8a7553 | -20.95375 | -56.59987 | 2025-05-22 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fb4f58a-8cc6-30ee-b762-bdd47e1afe54 | -22.16251 | -42.94481 | 2025-05-22 04:49:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6c919d32-4aba-3ea4-ba15-c33b32dcc6c9 | -21.48311 | -57.11733 | 2025-05-22 04:49:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25869202-d803-3a40-a75f-894be6584e35 | -20.94891 | -56.58654 | 2025-05-22 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c78ccb35-c9a5-35b2-90c2-e86a8a2d83b2 | -22.95304 | -49.10559 | 2025-05-22 04:49:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29ccdcef-a257-392c-ac29-7e93e22a84e5 | -21.36336 | -48.76432 | 2025-05-22 04:49:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdab7865-4ab6-3b42-8725-6c5031407b85 | -21.48239 | -57.12148 | 2025-05-22 04:49:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 370b9815-ef97-3d69-a88e-28bd1163e89d | -19.05663 | -53.45784 | 2025-05-22 04:49:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69f8e339-3fee-3c74-8e4a-408cdc8c3662 | -19.90133 | -49.32907 | 2025-05-22 04:49:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dc0d1067-2edf-3b5b-9b79-65fde2ad87ed | -21.21785 | -48.61263 | 2025-05-22 04:49:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 17746eb7-055a-306c-9bbc-14cc754bc470 | -20.94479 | -56.58985 | 2025-05-22 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5f1d652b-dee7-3ef5-a1a5-bf71a0bb95f5 | -23.62227 | -46.4965 | 2025-05-22 04:49:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 37dde37a-7146-3437-84e7-a7ea483f6426 | -21.46259 | -57.17327 | 2025-05-22 04:49:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1566e148-2f77-33d7-94cd-3d0b35e57eb7 | -19.73652 | -54.50892 | 2025-05-22 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4465d834-56d1-3c08-8e43-cff69f477908 | -22.5408 | -48.8135 | 2025-05-22 04:49:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| beabf49d-0aff-34be-ab90-a13a9b54030a | -20.60339 | -48.87127 | 2025-05-22 04:49:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 23a75faa-eeb9-3496-8a84-52c16feddbc7 | -19.73593 | -54.5126 | 2025-05-22 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d922064-4a46-3437-9fd6-2317ff3b7014 | -19.06051 | -53.45476 | 2025-05-22 04:49:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 586853eb-9f29-3f63-9b01-efbc60e3a0f9 | -19.05719 | -53.45419 | 2025-05-22 04:49:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbeb16c7-3808-3328-95a0-afdf71ae9291 | -21.70452 | -55.49241 | 2025-05-22 04:49:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d8fca07c-b16e-33bb-bbf2-5651d224ed62 | -19.05995 | -53.45841 | 2025-05-22 04:49:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dcfa42ca-cb4a-32fb-9f58-24f487af57c8 | -19.02381 | -57.62004 | 2025-05-22 04:49:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 09801f83-7918-3eda-8262-cee69857db58 | -21.4633 | -57.16917 | 2025-05-22 04:49:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69a4687f-ed0d-3384-b296-a46493dd98de | -19.06327 | -53.45898 | 2025-05-22 04:49:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 815c2327-8ee8-3c0f-bd20-3eb148cd659b | -19.97231 | -47.18845 | 2025-05-22 04:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 454ef46e-0417-3bc6-b037-7dab07637ed4 | -19.73261 | -54.512 | 2025-05-22 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71328925-4c45-348c-a502-a56d23300d6b | -20.60793 | -48.86808 | 2025-05-22 04:49:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 286c8ff2-0e84-30df-9621-57a3dab5f1e0 | -19.88003 | -54.65057 | 2025-05-22 04:49:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccd36915-92a3-302b-814d-ab6fc468f744 | -20.95308 | -56.60385 | 2025-05-22 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91d30d88-826b-31fa-ba7b-393a43b44ef3 | -22.16176 | -42.94325 | 2025-05-22 04:49:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 32c110b0-e790-3c0d-838f-f3e5bb6f81bb | -20.60746 | -48.87186 | 2025-05-22 04:49:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |


[Clique aqui para ver as próximas entradas](README20.md)
