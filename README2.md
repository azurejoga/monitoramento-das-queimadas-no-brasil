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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be992524-064b-3aee-894b-79a3871b7cbf | -21.5242 | -47.121201 | 2025-02-18 00:48:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d481e03a-140d-3ec3-89e5-d8c686d525f7 | -19.118099 | -56.214001 | 2025-02-18 00:48:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a41b918a-5ae3-3b7d-a4fe-1def5e0446fb | -19.127899 | -56.2118 | 2025-02-18 00:48:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 089d1c3b-4f62-3bae-909e-31e13f992316 | -21.0826 | -56.3634 | 2025-02-18 00:48:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 62678947-036c-3a59-a350-bc7a4efc6242 | -21.9634 | -57.558601 | 2025-02-18 00:48:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 16817609-3d38-3ffc-a102-c24c2d75234c | -20.9041 | -56.548302 | 2025-02-18 00:48:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5e25a45f-0c97-3b77-9084-70bbb4aa7946 | -21.072901 | -56.365501 | 2025-02-18 00:48:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6d13bb7a-c97c-32d5-a58f-3389dd226c53 | -12.3289 | -52.4674 | 2025-02-18 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e553bb03-446f-303c-a0ff-cab75077d73f | -21.4203 | -48.539001 | 2025-02-18 00:48:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5580c06c-16a7-3623-9f72-fd9fdcaaf5c9 | -20.4314 | -55.6819 | 2025-02-18 00:48:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bb4c61ce-055d-3f2c-a412-51a062ec4ff0 | -21.373699 | -48.560902 | 2025-02-18 00:48:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 28f00a57-d1b5-3ffc-b96c-e4b497c98d1f | -21.371599 | -48.552101 | 2025-02-18 00:48:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d3a1807-7dea-3547-acdf-bab2649dd198 | -19.1243 | -56.193401 | 2025-02-18 00:48:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5124160a-3509-3979-a9d5-86379e572437 | -19.1145 | -56.195499 | 2025-02-18 00:48:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 20b5aa47-392a-320e-b380-9b00bbcee865 | -10.5981 | -45.079201 | 2025-02-18 00:48:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d622d0f1-2b10-388e-870e-6b63cba07c50 | -12.3306 | -52.474701 | 2025-02-18 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d750cb5c-7663-39dd-b182-47978d1442f5 | -20.9198 | -56.5238 | 2025-02-18 00:48:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1e2c29c6-4243-32eb-95f4-0d2bf4daf472 | -21.3654 | -48.525799 | 2025-02-18 00:48:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 56f0d530-6d10-389d-9f3f-c5e87d0b1735 | -21.3834 | -48.5583 | 2025-02-18 00:48:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2be2c1d-78eb-3fba-9792-f9b808c2150c | -21.4182 | -48.5303 | 2025-02-18 00:48:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5d2d6f0f-2fbb-3f9a-845c-22ed73e02056 | -21.0748 | -56.3755 | 2025-02-18 00:48:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c7b67536-9a8a-33ec-8c9d-8dd016faf31a | -19.116301 | -56.2048 | 2025-02-18 00:48:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6692c196-9b74-34fb-a6d4-4ec5a38baef7 | -19.126101 | -56.202599 | 2025-02-18 00:48:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6fded9d5-9b45-311d-9bd0-5688b8f7a82e | -20.9217 | -56.533901 | 2025-02-18 00:48:00 | METOP-B | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 75d2bc68-b7db-3237-bc87-4e9059f5a3b7 | -14.9892 | -50.7509 | 2025-02-18 00:49:00 | METOP-B | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f53ba8f2-9663-311e-8623-d95e9042faae | -19.0741 | -56.042702 | 2025-02-18 00:49:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 458cdf57-9b38-30d5-8cd8-111420fd136a | -10.6079 | -45.076599 | 2025-02-18 00:49:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4402869c-9a1a-3d07-a921-fb7a47d17cd6 | -14.9911 | -50.7589 | 2025-02-18 00:49:00 | METOP-B | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4843f050-d50c-3f9f-bfef-51a836d04d10 | -19.0644 | -56.0448 | 2025-02-18 00:49:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 65fa51a8-6d91-3d3c-bd02-0832aa6eab61 | -14.9813 | -50.761299 | 2025-02-18 00:49:00 | METOP-B | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dd385f4c-3520-3734-97cb-6df61a733849 | -19.0723 | -56.033699 | 2025-02-18 00:49:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 15b22619-babe-3ee0-ac17-d722cd3ed189 | -11.2511 | -48.980099 | 2025-02-18 00:49:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e290f210-d826-3c0f-b70d-e6a886408289 | -10.613 | -45.096802 | 2025-02-18 00:49:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 309f8c92-09a7-39f9-98cc-6caaa716cd0c | -11.2537 | -48.991001 | 2025-02-18 00:49:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5398e441-7b98-3d47-ba6a-d59315162e9b | -19.075899 | -56.051701 | 2025-02-18 00:49:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fca2e3d5-f480-30fe-aa30-efd189b27272 | -10.6 | -45.1158 | 2025-02-18 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| a3c25135-b511-391c-b973-a5bf00605d6c | -19.1353 | -56.2324 | 2025-02-18 00:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 650465b7-71d3-3f32-8160-b5788ff67468 | -10.6191 | -45.1132 | 2025-02-18 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 8fc89eaa-58de-341a-b4fe-3c8bb72aa307 | -10.6195 | -45.0902 | 2025-02-18 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 062ce57c-d3df-3ac9-a23e-8c08755edcff | -19.1157 | -56.2142 | 2025-02-18 00:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 91cfdb47-393c-35e1-9d65-66dbee60bc85 | -19.1357 | -56.2114 | 2025-02-18 00:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 23262305-0384-312d-9c92-fa4582b8b293 | -19.1153 | -56.2352 | 2025-02-18 00:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| bc1ff2bc-8776-3699-b0a6-cd3c2ebe21af | -10.6191 | -45.1132 | 2025-02-18 01:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f27ba345-d583-3083-a65d-70a98de982d7 | -19.1157 | -56.2142 | 2025-02-18 01:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.6 |
| 243a0b9c-8633-3398-af0b-d4326e02cbfc | -10.6195 | -45.0902 | 2025-02-18 01:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6b45941e-3942-3634-85d1-e7f482893cf4 | -19.1153 | -56.2352 | 2025-02-18 01:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 1b5c0045-16aa-3e6d-9db3-500fe65bcde2 | -10.6 | -45.1158 | 2025-02-18 01:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 9a58fb33-5b33-3952-8591-8e0ed30b6136 | -19.1353 | -56.2324 | 2025-02-18 01:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| c5148c27-0ecd-395c-8996-937178f440bc | -19.1357 | -56.2114 | 2025-02-18 01:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.1 |
| de326e29-86ff-30cc-b21d-bcc8f532b351 | -19.0785 | -56.0727 | 2025-02-18 01:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.0 |
| 2de95ff4-1ee8-392d-b8f4-3091e32b0084 | -10.6 | -45.1158 | 2025-02-18 01:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| b22c1a0e-fe56-3e12-bc09-ee62153765c8 | -19.1157 | -56.2142 | 2025-02-18 01:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 0eb0d1c7-addc-3c53-873a-ac17f0990772 | -19.1153 | -56.2352 | 2025-02-18 01:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| dd15e1ee-a362-31b0-ad4c-a293c9eece64 | -10.6191 | -45.1132 | 2025-02-18 01:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 85b99f37-f342-376f-bfa1-3e64cfca816c | -19.0789 | -56.0516 | 2025-02-18 01:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 67e4ba0c-c640-30e9-b05d-5667f6782f8a | -19.1353 | -56.2324 | 2025-02-18 01:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| bbdb534a-69f5-30ae-bd73-2fdf3439befe | -19.1357 | -56.2114 | 2025-02-18 01:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.2 |
| cc1b7fca-34ce-380e-a46f-54005d6a94c0 | -10.6 | -45.1158 | 2025-02-18 01:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 670644cb-e485-3601-adb5-2ae1aaa9ef00 | -19.1153 | -56.2352 | 2025-02-18 01:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.7 |
| d953c62e-6afc-3da3-91d6-03714bc88ea4 | -10.6191 | -45.1132 | 2025-02-18 01:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e0b4f36d-1851-3df8-a201-21d6f8173785 | -19.1357 | -56.2114 | 2025-02-18 01:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.5 |
| 0d9140fb-723b-39a2-8ea1-1c4bb36671db | -19.1157 | -56.2142 | 2025-02-18 01:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 78742020-733d-305e-aa48-09f9c378749a | -19.1353 | -56.2324 | 2025-02-18 01:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 7c346958-77b4-3899-adb2-93469bd07829 | -19.1157 | -56.2142 | 2025-02-18 01:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.0 |
| e2a23d80-6561-3c7c-a259-aeb1e0eb4e70 | -19.1353 | -56.2324 | 2025-02-18 01:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 11992e5d-33e8-3f93-8e98-9a866c91c19c | -10.6191 | -45.1132 | 2025-02-18 01:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 79a67847-b307-37d1-a8f4-525551da8ff8 | -19.1357 | -56.2114 | 2025-02-18 01:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.0 |
| f85adf2c-1955-3992-9459-4b2a6beb4265 | -19.1153 | -56.2352 | 2025-02-18 01:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.2 |
| cc9fc440-23ac-3fab-9a62-e67af05fbe97 | -19.1157 | -56.2142 | 2025-02-18 01:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 82524b27-6bdc-326d-bbd9-848f963c2187 | -19.1357 | -56.2114 | 2025-02-18 01:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.4 |
| cfbeb011-eae6-333d-b0db-4eca4c7b9d65 | -19.1353 | -56.2324 | 2025-02-18 01:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 1111f77b-dc66-3542-9fbf-3c81574eae7a | -19.1153 | -56.2352 | 2025-02-18 01:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 40ab8d93-1623-3e5b-9ee4-b39b004ed056 | -19.124701 | -56.219799 | 2025-02-18 01:42:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 89b00d5a-cdf8-3c60-9065-a079d1225012 | -21.0744 | -56.379002 | 2025-02-18 01:42:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 826e1147-3786-3296-bdd4-035e0f1759f7 | -21.076799 | -56.388802 | 2025-02-18 01:42:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fc33c563-3951-3dba-ac01-c489ebf25650 | -20.916599 | -56.538101 | 2025-02-18 01:42:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c42e761d-05d0-3c7a-9f76-5f595b484d8f | -19.127399 | -56.230499 | 2025-02-18 01:42:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 40fa4be4-27e2-34c5-af9c-b4350595036e | -19.134399 | -56.217201 | 2025-02-18 01:42:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b844d317-f7ab-3aaf-8ca7-99be7210ffc6 | -20.9116 | -56.5602 | 2025-02-18 01:42:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9b8ea61a-08f3-3f7f-b66e-adced3a0661b | -19.122101 | -56.209202 | 2025-02-18 01:42:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f7159cff-cb28-3dab-b3f9-3a362437d6fd | -21.9685 | -57.583099 | 2025-02-18 01:42:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3e32e625-1129-32f4-abce-3d4905764a69 | -21.966499 | -57.574501 | 2025-02-18 01:42:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3ffbc8ad-400d-3b1f-b174-2bd29ed6c071 | -20.9263 | -56.5354 | 2025-02-18 01:42:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| df53a852-e963-3549-9b44-72a497afeb44 | -19.1153 | -56.2352 | 2025-02-18 02:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| c011f91d-89a4-3946-9103-c2face528318 | -19.1353 | -56.2324 | 2025-02-18 02:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 848fa502-9739-33b5-9df6-baaa1fc76da4 | -19.1157 | -56.2142 | 2025-02-18 02:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 68ea24a9-28db-326c-aae5-3bc251062764 | -19.1231 | -56.23198 | 2025-02-18 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| ad711913-1e62-3cc8-afc9-faf49e6d47e3 | -19.11485 | -56.22697 | 2025-02-18 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 918ba3d7-bd36-34b4-ad16-534d1e899052 | -19.0627 | -56.05268 | 2025-02-18 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.0 |
| 7399c3ad-5915-333c-a699-adc7ff55391c | -19.07227 | -56.05748 | 2025-02-18 02:04:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 9426d1f9-ae48-3a35-b97b-1c368453f696 | -19.1353 | -56.2324 | 2025-02-18 02:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.1 |
| ad73f7bd-5848-353b-8387-afc10173405a | -19.1157 | -56.2142 | 2025-02-18 02:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| e1e7a0bd-5a02-3dcb-9d9a-b7b6674c19aa | -19.1153 | -56.2352 | 2025-02-18 02:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| a8dc78b6-60fb-3532-8c70-02083ff6eb6d | -20.61088 | -40.99117 | 2025-02-18 03:02:00 | NOAA-21 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 70430b22-9fca-3f83-a191-26a9e5816d12 | -19.16796 | -40.13546 | 2025-02-18 03:02:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f564d152-e0d5-3dba-89be-0512949d4dd1 | -10.18083 | -36.45924 | 2025-02-18 03:23:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4b4aa8e4-b019-3646-8eb7-d79e53716cfe | -6.61312 | -36.17805 | 2025-02-18 03:23:00 | NPP-375D | CUITÉ | PARAÍBA | Brasil | 2505105 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6037045d-f910-349d-b36e-f8082124a9dd | -9.73196 | -37.25436 | 2025-02-18 03:23:00 | NPP-375D | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cdf570c9-675f-3df3-8003-5e626955a610 | -6.6944 | -42.13612 | 2025-02-18 03:23:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bdf39782-4384-3176-b130-c54574a4480e | -5.25186 | -35.86877 | 2025-02-18 03:23:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
