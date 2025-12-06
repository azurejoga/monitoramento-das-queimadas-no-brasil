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
| 6597edf0-574f-37a1-885f-197a422e41f5 | -19.65303 | -56.86395 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b3292aef-b216-3e1e-b057-037fd9f0884e | -21.56963 | -43.98817 | 2025-12-06 04:16:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e44a5c7b-870f-3262-9ae1-5b836ffcfee2 | -19.66094 | -56.82901 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b9430e0d-e3a8-39d1-ae7e-da4fef3ac704 | -21.55011 | -44.29883 | 2025-12-06 04:16:00 | NPP-375D | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 55b90c6b-a73f-327e-91aa-4df69da6ef84 | -23.3685 | -51.40238 | 2025-12-06 04:16:00 | NPP-375D | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 093cb4d6-0d9f-33b2-8d08-9f2f9972fdbc | -19.59595 | -44.12439 | 2025-12-06 04:16:00 | NPP-375D | CAPIM BRANCO | MINAS GERAIS | Brasil | 3112505 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 860e6fd4-b3b6-3864-a274-58b4b73ed7f5 | -22.07893 | -46.82211 | 2025-12-06 04:16:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36ea7a79-d863-362c-a1ea-176e1f2e9c80 | -20.9183 | -49.23841 | 2025-12-06 04:16:00 | NPP-375D | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6f1e5585-b84a-3931-86be-8a53ec910840 | -19.87865 | -44.05162 | 2025-12-06 04:16:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2d2c28e9-72d2-3e72-b91c-8d054271367e | -19.64806 | -56.85735 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 677b9ab7-fa27-30f4-80a9-adacd4682ed0 | -22.98923 | -48.65583 | 2025-12-06 04:16:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd776131-87fa-3f3e-84e5-da8e4821862d | -19.64876 | -56.8258 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 76188bed-fd60-3453-85aa-3ac3e0216ab3 | -22.90164 | -47.18835 | 2025-12-06 04:16:00 | NPP-375D | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b5431168-db97-3e8e-8b11-a3672f2ca498 | -22.89757 | -47.19163 | 2025-12-06 04:16:00 | NPP-375D | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 10e9d82c-f4fb-3e3d-a463-7e124519e670 | -23.59081 | -46.35294 | 2025-12-06 04:16:00 | NPP-375D | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 34361989-5880-3395-beca-17e713c06fcb | -19.31713 | -41.59763 | 2025-12-06 04:16:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c1b01a92-257c-30ae-a017-08fe83ff52bb | -22.73161 | -49.34518 | 2025-12-06 04:16:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 220a756d-88a1-380f-a558-745f702d77f6 | -19.31874 | -41.60021 | 2025-12-06 04:16:00 | NPP-375D | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 16413b5c-e65f-325e-b5db-e5ee1e6fc8a5 | -22.72998 | -49.34764 | 2025-12-06 04:16:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 00d48f12-978f-3eb4-89c4-05da78306c14 | -22.90097 | -47.19229 | 2025-12-06 04:16:00 | NPP-375D | HORTOLÂNDIA | SÃO PAULO | Brasil | 3519071 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7a7c74ee-309c-33aa-935c-a7d3fd6f6c71 | -24.16516 | -49.57692 | 2025-12-06 04:16:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d3d129c4-70d7-3522-9dcc-651b55a8a56d | -19.67312 | -56.82548 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 965238ee-4a62-3e68-a38f-2d2e7198724a | -22.90049 | -46.22512 | 2025-12-06 04:16:00 | NPP-375D | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 1916f2eb-8ff9-3f0c-9a81-86508b4a4b4f | -24.10287 | -50.12711 | 2025-12-06 04:16:00 | NPP-375D | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 12537fcc-a425-33df-8a13-375642b2b538 | -20.9174 | -49.24326 | 2025-12-06 04:16:00 | NPP-375D | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f14ae70c-e7b3-317c-a168-bbaa74197abb | -19.64153 | -56.82915 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 681e5689-e4a0-3961-899a-591a01cc76a5 | -22.78177 | -43.04428 | 2025-12-06 04:16:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bc5c3ff1-fa23-33e8-8f72-a244966e2655 | -23.43867 | -47.05622 | 2025-12-06 04:16:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 00ebb5a8-9226-3732-9706-26d47cd7c28e | -19.64643 | -56.82904 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c7bdae02-3e6e-3546-9313-084a124b74a6 | -19.49448 | -44.27696 | 2025-12-06 04:16:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12b6d041-23a1-3700-a0ef-00818d9b24b1 | -22.4273 | -48.56452 | 2025-12-06 04:16:00 | NPP-375D | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 77886741-2da5-3981-a2b1-b2c34fe207c0 | -19.65165 | -56.86208 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f66d17cb-246c-3340-b5da-3e7aafeba992 | -22.78264 | -43.04266 | 2025-12-06 04:16:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0141ac0d-ac3a-3e92-9f0c-1af90a2144b5 | -20.32899 | -50.19221 | 2025-12-06 04:16:00 | NPP-375D | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a6322981-61eb-3f49-b9b8-9ddaaeee9611 | -24.16883 | -49.57767 | 2025-12-06 04:16:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fcc7bb3e-4db1-3ae7-86be-9902d97db9f9 | -20.3857 | -44.75166 | 2025-12-06 04:16:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bd12654c-237a-38c9-b480-76ca9f50acd0 | -22.08232 | -46.82273 | 2025-12-06 04:16:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fe03b74-b6c5-30b3-b60a-588eca870505 | -19.64763 | -56.83076 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| aab501c6-f9f7-3e8f-acc1-e97b9ae135e7 | -22.90382 | -46.22576 | 2025-12-06 04:16:00 | NPP-375D | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| a95f31f4-495e-3810-a124-7bd48f843040 | -20.92245 | -56.37888 | 2025-12-06 04:16:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cf1c032-a8cb-3a20-8dc9-bc50248caee9 | -22.30181 | -46.90659 | 2025-12-06 04:16:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e9dc9e3-f675-392f-bb85-ed4590024eac | -20.92144 | -56.38332 | 2025-12-06 04:16:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4327b2c1-9494-33ba-8179-1ca9d3bc7043 | -19.66815 | -56.82565 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 836c8a64-b108-38ad-99c0-ec14085c49b8 | -19.65485 | -56.82741 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 14e1960a-3f2a-3537-9534-4bd076fd45ca | -20.32829 | -50.1959 | 2025-12-06 04:16:00 | NPP-375D | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75117481-ec08-3c8b-8e35-62865caa8f23 | -19.65252 | -56.83064 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f536272f-73a5-30a9-8de9-966a95691eed | -22.73072 | -49.34997 | 2025-12-06 04:16:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80701c8d-6151-38bf-9813-9dbff843281f | -21.18317 | -45.60973 | 2025-12-06 04:16:00 | NPP-375D | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 496511d3-520d-38ee-ae32-b98bb0e84a67 | -22.48141 | -47.06449 | 2025-12-06 04:16:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| adaed416-c5b0-3d60-bfc3-fda02406d068 | -24.16603 | -49.57219 | 2025-12-06 04:16:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 6.3 |
| be22c82f-a395-3be9-9d45-c7b398b989b6 | -24.10138 | -50.12841 | 2025-12-06 04:16:00 | NPP-375D | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4e70233e-5d53-3817-9f42-bf4a720767be | -20.91566 | -56.38174 | 2025-12-06 04:16:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 021a409b-0e5c-312b-a556-191de7c6b87d | -19.66703 | -56.82389 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 84e1be2f-57a1-36e6-bd9e-c4021c6f35a2 | -21.27156 | -47.10461 | 2025-12-06 04:16:00 | NPP-375D | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 28b1ac3b-5086-30ac-a702-475c71f15585 | -20.32425 | -50.19512 | 2025-12-06 04:16:00 | NPP-375D | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3b141648-b03d-376c-a3e3-c7982ab8a643 | -20.91665 | -56.37739 | 2025-12-06 04:16:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ce902f8-c3d3-3bf4-951d-597582f2055e | -21.65186 | -44.38535 | 2025-12-06 04:16:00 | NPP-375D | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2291354f-d55b-3186-9075-28aea9044e3d | -19.65369 | -56.82568 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fc155357-5dd6-3688-99b2-16021560cab1 | -19.66207 | -56.82403 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a26f0873-8f25-3659-9003-af6466201984 | -19.23561 | -45.35072 | 2025-12-06 04:16:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ad6bbf1-6713-3ca7-95e8-df21f5dd2c1b | -21.3336 | -44.95338 | 2025-12-06 04:16:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f3695338-9e8f-3bcb-8901-5442d31be936 | -19.64692 | -56.86236 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7b7a03a1-8272-384c-8dd1-99224565eebf | -19.67424 | -56.82726 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 77af4427-3a8e-3f99-889f-913249097063 | -22.63991 | -52.02701 | 2025-12-06 04:16:00 | NPP-375D | PARANAPOEMA | PARANÁ | Brasil | 4118303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5ed35716-0787-3b36-9e97-eba7d374f2d6 | -22.75139 | -42.00233 | 2025-12-06 04:16:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6fb5eaf7-9c01-3111-b1f4-20160532910f | -20.68735 | -48.80129 | 2025-12-06 04:16:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5af2e46c-c8b9-3895-9da1-789d63974a45 | -19.64527 | -56.834 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 489f7dd5-f10d-3a03-bb20-0ec36de43bf1 | -19.65978 | -56.82726 | 2025-12-06 04:16:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2cc2a985-367c-35a9-a257-daa614e3137b | -28.16925 | -49.05495 | 2025-12-06 04:18:00 | NPP-375D | ARMAZÉM | SANTA CATARINA | Brasil | 4201505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7fb8ae6d-ba21-3545-894e-54c5c25434f9 | -26.23135 | -50.36493 | 2025-12-06 04:18:00 | NPP-375D | CANOINHAS | SANTA CATARINA | Brasil | 4203808 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b0a00650-1e12-3b2c-a6d9-8e0b9033f42d | -29.56143 | -49.91754 | 2025-12-06 04:18:00 | NPP-375D | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 7e0d0569-d009-3c2c-aef1-dd724f865493 | -26.1547 | -51.4957 | 2025-12-06 04:18:00 | NPP-375D | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 32e833c8-5b5f-376e-a515-e02dccc44a37 | -25.336 | -49.87789 | 2025-12-06 04:18:00 | NPP-375D | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8e2de427-7ccb-3d4e-abe1-d208e9f4ccba | -25.33514 | -49.88263 | 2025-12-06 04:18:00 | NPP-375D | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e81153fc-68ae-392d-86af-68f6268b3d4a | -27.29532 | -53.04895 | 2025-12-06 04:18:00 | NPP-375D | PLANALTO | RIO GRANDE DO SUL | Brasil | 4314704 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 824d9d1b-ec94-3467-897c-764c71b819aa | -26.41381 | -51.84233 | 2025-12-06 04:18:00 | NPP-375D | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 70aec9f4-f7d4-32fb-9959-31400ba5dd8f | -26.15861 | -51.49664 | 2025-12-06 04:18:00 | NPP-375D | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2cdf4b75-2fb8-3159-ab8f-921a39071156 | -29.55795 | -49.91672 | 2025-12-06 04:18:00 | NPP-375D | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 3.9 |
| 1d543ee8-96e7-3010-be97-9483a62a8334 | -27.32018 | -50.55146 | 2025-12-06 04:18:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 43.5 |
| e7fac035-d5ee-3da1-9ae1-58f565473e98 | -29.92643 | -51.21099 | 2025-12-06 04:18:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 4.6 |
| dcd0bdf6-962c-3795-9dd3-c03d0fce7425 | -27.45243 | -50.34293 | 2025-12-06 04:18:00 | NPP-375D | PONTE ALTA | SANTA CATARINA | Brasil | 4213302 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 492b08f5-4400-3460-8b67-a4afd66fcf02 | -25.33236 | -49.87702 | 2025-12-06 04:18:00 | NPP-375D | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e6fd84f2-5028-37eb-9751-451fc9beea65 | -28.17269 | -49.05569 | 2025-12-06 04:18:00 | NPP-375D | ARMAZÉM | SANTA CATARINA | Brasil | 4201505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 133caf0c-fbd9-3435-bc03-1c8f4b9d365c | 3.4515 | -51.25655 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a4d4ee7-6cdc-3532-bfc4-ac8d479902b9 | 3.49673 | -51.24578 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1ac338b1-5769-3ec9-9961-b83f7a588965 | 3.41459 | -51.26609 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ef4932a-ce35-3a79-bcc4-6d4a697cbf75 | 3.47 | -51.23823 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34efd0f1-2f4e-3d10-affd-a3ad4e277658 | 3.46642 | -51.24265 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5fb96af5-5996-3d2f-8fc6-805017c65f9b | 3.42235 | -51.26102 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 595df4c0-7c18-329b-8ea6-9967768c559c | 3.4884 | -51.24704 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecc67483-498d-3066-9643-905227abc530 | 3.45868 | -51.2477 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2ecee0d1-b038-3603-9c22-070b31752a5a | 3.45093 | -51.25277 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6e6af38-d660-39c8-a7df-df5b19d2914f | 3.42594 | -51.25659 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 03f637c9-b985-3184-a6b1-7f82f56103af | 3.66277 | -51.27986 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cfc1e3a-9425-317d-af53-06749e487887 | 3.50787 | -51.25198 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 74ed0771-df9a-3c60-997f-15c84153afb1 | 3.48952 | -51.24315 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f0e4186-5634-3c7c-b275-5c08946e8111 | 3.509 | -51.25958 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc76a781-d788-3bcf-9a03-69802f7e4f6d | 3.49841 | -51.24567 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2d2aea06-f94f-31c8-9064-3b3e072662f7 | 3.50843 | -51.25578 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f8b0d451-f085-3eb6-8f47-873b2066bc29 | 3.471 | -51.49846 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README6.md)
