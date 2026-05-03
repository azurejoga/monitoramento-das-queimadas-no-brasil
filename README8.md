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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1d9a4d8-bb4f-3b23-8d65-06fa226d147e | -9.27992 | -56.24513 | 2026-05-03 05:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bf5bb6f-05bc-3e4b-a876-7e8fad2d4127 | -13.22741 | -54.54152 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf66faf5-e4c7-31d0-9e01-d8120416a832 | -11.88156 | -43.805 | 2026-05-03 05:01:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f559ce59-e8d9-372e-a48f-d456517f9429 | -12.28792 | -57.39826 | 2026-05-03 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52a6f2b4-16a4-37eb-8680-69e16e05e15d | -12.29133 | -57.39885 | 2026-05-03 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08c53224-de24-3dc4-be67-192f071cdbe4 | -11.55614 | -48.26896 | 2026-05-03 05:01:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91c7891a-da75-398f-b4f4-63058dd2c716 | -10.97594 | -45.09433 | 2026-05-03 05:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5195e766-aef3-3a77-a391-dbefc224659d | -13.2207 | -54.54046 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89d23fc3-5c93-36e1-9a0c-51df340eb898 | -12.23048 | -54.381 | 2026-05-03 05:01:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e5e1e67-15af-33f2-8510-585252922828 | -13.20952 | -54.54612 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54080203-427e-33e4-80de-b78f412a3a0c | -11.30786 | -54.7305 | 2026-05-03 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fba2549-1fbb-31a1-a9d4-26527099bb25 | -11.30454 | -54.72997 | 2026-05-03 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93c7fbc9-854c-3efa-8c9c-6d2c7cbf19c6 | -13.21232 | -54.55027 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90806321-1ad5-3c08-b0b9-dd8dd1622b09 | -13.21679 | -54.54356 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84615933-110e-32c8-90f9-02a001f1cf0b | -13.19667 | -54.54034 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f21e1ca-6332-3de7-ac96-89d8881c46ce | -9.71992 | -60.2022 | 2026-05-03 05:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4de7b22e-fbf3-3284-94b7-0704141fd205 | -13.20002 | -54.54088 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f58ab689-dc90-3d4e-918c-f833059f88d7 | -13.22572 | -54.53009 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d9982e8-42b6-3e87-bec6-812a67e5e15b | -16.10805 | -49.23767 | 2026-05-03 05:01:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f907b0d5-6435-37cd-bb9f-bcbe2d663b1b | -11.30399 | -54.73349 | 2026-05-03 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1299797c-ef0a-3bad-8984-9e3e47058b62 | -12.36139 | -50.02582 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 365deb8b-d610-39c0-9a05-0f4611bbc342 | -12.28576 | -57.39015 | 2026-05-03 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 586a7342-6d03-392e-a65c-c201ef782143 | -12.22769 | -54.37687 | 2026-05-03 05:01:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c187d4e1-e9d0-3c6f-ad2b-c3ca882bb337 | -12.36502 | -50.03018 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 56808875-ce9a-33e6-9178-1636918327dc | -13.99852 | -56.63264 | 2026-05-03 05:01:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51a7f3b1-051b-3649-8beb-b7ad623c3bff | -13.21566 | -54.5285 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a57fbc4-4453-38c4-929d-73a9d2edd7b3 | -13.21846 | -54.53267 | 2026-05-03 05:01:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f214a608-4e2c-39e7-b99f-9fef52917937 | -10.98158 | -45.09521 | 2026-05-03 05:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7468c6f6-0b08-3c23-9c73-12c66fb60f08 | -10.98256 | -45.0874 | 2026-05-03 05:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e536f5eb-89bd-3053-9455-29832c8c3f01 | -12.37901 | -50.02055 | 2026-05-03 05:01:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47d8748e-5480-3e2a-b98c-221a1337aeff | -10.98723 | -45.09603 | 2026-05-03 05:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dfd66bf7-b4e3-3028-879d-31a8fa910cda | -14.05335 | -53.40203 | 2026-05-03 05:01:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45935f1f-6cb8-3cc1-a59a-bcfd1bcb9403 | -18.05868 | -52.94778 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 866c53d3-4784-3ec2-95ab-8c4e1b02a48b | -17.99614 | -52.97906 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 348a75b6-b08c-3a48-9348-03c54e89d0bc | -17.99987 | -52.97963 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1c3c925-3fe9-34e3-aa2e-87e9d53c2afb | -17.99678 | -52.97441 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 166c0f95-1fb6-33b6-ac75-5d21ba23bc03 | -18.05796 | -52.94541 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 762d7fba-1c34-3f46-b040-54b19e5e77bc | -20.22554 | -50.91612 | 2026-05-03 05:04:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b79cff60-364d-38cd-b455-b82b5d607592 | -17.95142 | -52.97223 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d3e6628-1911-352c-be27-0e167f05bb2b | -17.87766 | -55.26112 | 2026-05-03 05:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0f0d4700-2d93-3731-882c-ca3631de3bac | -20.18331 | -46.45187 | 2026-05-03 05:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48b6a464-00bf-31ed-b771-dae351e0d6c8 | -17.95205 | -52.96761 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e51ba4ee-465d-3b3f-9504-6c17e43eb321 | -20.18805 | -46.46349 | 2026-05-03 05:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62716999-f22f-3dfa-bb4a-274f0ce8d9cd | -17.99922 | -52.98428 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da15dd0f-b003-3f53-a240-d2c662e5d5ff | -18.05932 | -52.94307 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5244a558-6f75-38c9-a477-a5c9201c2041 | -17.95017 | -52.97013 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8caa278-3453-3297-8e68-3459517dcead | -18.2535 | -51.2619 | 2026-05-03 05:04:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c441c216-c010-3d07-ab0f-ce187f2c5db9 | -17.9539 | -52.9707 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddad4270-fc53-3589-8ab8-932a9c7c9765 | -17.95063 | -52.99382 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acfc813a-3690-33a5-b4fe-d2e885f8e3ef | -17.88161 | -55.2579 | 2026-05-03 05:04:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cd5d87c8-f964-3925-8559-77ea159f580d | -20.19382 | -46.46448 | 2026-05-03 05:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36b6b3a3-54d7-33de-80ff-0ee680a0392e | -17.94955 | -52.98613 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 323f9842-0832-31ba-8d8d-7b0a08075aab | -18.05495 | -52.94721 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5d3d5a9-4571-38e6-a920-d65cf775e281 | -17.95202 | -52.99596 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f2ae4d4-8159-3637-bd7d-ab51d626fead | -17.95264 | -52.99132 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24185373-35ed-3983-98b8-8fd2622f7fe1 | -17.95578 | -52.96818 | 2026-05-03 05:04:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad3a1f32-ab80-3501-b768-7e7fefbe60fb | -12.37 | -50.0242 | 2026-05-03 05:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 729ba4cb-a83f-3710-ac43-e2b0958904a3 | -12.37 | -50.0242 | 2026-05-03 05:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 2fb5e295-1c21-3171-8cb9-a98aad098cf5 | -13.2183 | -54.5388 | 2026-05-03 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 9c830d44-6c39-3d1e-80bc-4bf534c94689 | -13.1992 | -54.5408 | 2026-05-03 05:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 15d9092e-ee17-33a0-84c2-5aa3fd6440b4 | -13.2183 | -54.5388 | 2026-05-03 05:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| b5ed963c-fa88-36ec-94f1-ae290c9dbb62 | -12.37 | -50.0242 | 2026-05-03 05:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 4811fde9-5379-3ef8-ac0d-123464c566f5 | -12.37 | -50.0242 | 2026-05-03 05:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 9ff3ef9c-3780-3bdf-b5f2-14795f5aba02 | -13.2183 | -54.5388 | 2026-05-03 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 3fb18fca-92aa-376d-a992-0d81e4e201ca | 4.14727 | -61.27966 | 2026-05-03 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7039cfde-6d76-3fd2-ad5c-fe06ac19a48e | 4.14235 | -61.27195 | 2026-05-03 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b38e458-e54e-3b7d-8abc-bfbd3bd80b2d | 4.15541 | -61.26134 | 2026-05-03 05:46:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a7a80a0-cd7d-3f4c-8e09-60d33543ed9b | -12.37 | -50.0242 | 2026-05-03 05:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 43fd536d-ffd3-3646-84fb-12c98ffd55f7 | -13.2183 | -54.5388 | 2026-05-03 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| a65ca043-c7a3-3f58-9dbf-72bac47eaf79 | -13.2252 | -54.53233 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e1e239f-4425-3c25-9146-4785bd05098c | -13.21745 | -54.53868 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2db636c-e360-3ad9-9af7-d7d8061b7048 | -13.21899 | -54.54763 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6cfd5d17-b797-38a8-ac32-f4b0ff16f870 | -7.86769 | -61.49457 | 2026-05-03 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdef284e-4828-30ef-b55f-0a4bd0f29143 | -13.22042 | -54.53382 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee8ccecb-90a0-31b6-ad14-83be3071a60d | -13.21814 | -54.5316 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4be7709-0c28-3f97-a9ff-24700dfd606b | -13.22385 | -54.54618 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8114cb23-647b-30c6-a77f-b28ee4ef09c1 | -7.86714 | -61.49844 | 2026-05-03 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 986f1dc3-8e54-375e-bfc4-2f912361c43a | -13.21678 | -54.54555 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6da57d26-2286-3335-9126-0df973e2646c | -13.20629 | -54.53238 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e290cc84-8b37-3e99-9fdc-e6fb1c6473c0 | -13.21335 | -54.53317 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff42b5aa-6595-3e4f-a6d0-5986586a516a | -13.22452 | -54.53938 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dafe5b17-a1a8-399f-9a94-af4fa90fcd54 | -13.22749 | -54.53455 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82ddeb80-02dd-3e73-a58b-31593385f02a | -13.23455 | -54.53526 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d758073-df99-39c3-88a5-8c7c60e2fb65 | -13.21969 | -54.54083 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b9adbf9-06d7-32f0-a69d-c963efda238d | -13.22677 | -54.54146 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0a6f62ba-7ecd-383b-90b4-6f30e3fa2661 | -13.23159 | -54.54001 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 048e6757-d3cd-3930-a1e6-6885eeaf9fdc | -13.20557 | -54.53941 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13e0db20-5d58-3217-8ccd-795151c259a1 | -13.23226 | -54.53313 | 2026-05-03 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ccf2597-ce99-3f57-8e63-96f4b1f327cf | -13.2183 | -54.5388 | 2026-05-03 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 3b5a45e8-e819-3108-8ac9-ee4740564eff | -12.37 | -50.0242 | 2026-05-03 06:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 2a0a6ea5-4d0b-3d95-b56a-e653d3dd3478 | -11.87955 | -43.80598 | 2026-05-03 06:08:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37aee234-3d2e-341d-a72f-3602cda1fb73 | -10.97382 | -45.08609 | 2026-05-03 06:08:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d5d2697e-5fee-3081-b947-5b0cd796d7d1 | -10.97217 | -45.09631 | 2026-05-03 06:08:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b496359f-d050-3660-9c8d-25f55ec6c13c | -12.35241 | -50.01713 | 2026-05-03 06:08:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 51609b14-794f-375d-b658-3e27ebb1e804 | -12.27905 | -44.62875 | 2026-05-03 06:08:00 | AQUA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fa5fd366-4fb9-35be-af9a-19ad4b86381e | -10.98155 | -45.09775 | 2026-05-03 06:08:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| b7463a4d-c73c-3232-9822-f5d94b2991ab | -10.9832 | -45.08752 | 2026-05-03 06:08:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d2ed0545-89bb-378e-93dc-508f1e737a58 | -12.3475 | -50.02391 | 2026-05-03 06:08:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| bcae84db-91b2-38c6-b744-740ae8415536 | -12.36554 | -50.01962 | 2026-05-03 06:08:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| f04dabfc-0c99-30db-ae2d-3e4fb2a5ad2f | -12.36065 | -50.02629 | 2026-05-03 06:08:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |


[Clique aqui para ver as próximas entradas](README9.md)
