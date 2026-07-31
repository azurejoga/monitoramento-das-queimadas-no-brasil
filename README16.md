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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dd96169-9916-3971-98fa-c4a7e9e1bf77 | -12.5989 | -44.6381 | 2026-07-31 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 4ff5c075-7426-3a57-ba27-0dfe245b7e4e | -12.6186 | -44.6116 | 2026-07-31 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 221.7 |
| 3ad7fb7e-afff-3ab9-a8b1-9e0dc29dbd1c | -12.6191 | -44.5882 | 2026-07-31 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| d0c802b7-a673-325f-97a5-5612658cec62 | -12.6186 | -44.6116 | 2026-07-31 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 228.1 |
| deef9ac0-432f-34c6-8855-9aeeb9c6608b | -12.5989 | -44.6381 | 2026-07-31 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| ff0c1db7-7678-3b22-94cd-16e3c626474e | -14.1966 | -44.1029 | 2026-07-31 12:40:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 13ee3478-da31-3916-a5b1-a0e0f1d0d6fc | -12.58 | -44.6178 | 2026-07-31 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 4301bcb6-6f97-3d11-8304-3e074322d68c | -12.5993 | -44.6147 | 2026-07-31 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 359.1 |
| 09917257-d07c-3d79-9fcc-21342c2c0665 | -14.2162 | -44.0993 | 2026-07-31 12:40:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 346.6 |
| a912fe4d-56be-30ce-a519-23fb40cb4120 | -14.2162 | -44.0993 | 2026-07-31 12:50:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 198.3 |
| f241fca9-2604-39ad-b0b2-b291e15ccf42 | -14.1966 | -44.1029 | 2026-07-31 12:50:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| a0e943fe-7827-3e12-a0e4-9b33e47fac29 | -12.6191 | -44.5882 | 2026-07-31 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| a74eb824-95ff-363f-a2b3-8a2cb910f10f | -11.3 | -50.301 | 2026-07-31 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 1383b4c6-3cca-3406-a34e-a431748422c5 | -12.5989 | -44.6381 | 2026-07-31 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.6 |
| ba7c614d-13e3-39e7-a5ae-be8170326eb1 | -12.5993 | -44.6147 | 2026-07-31 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 399.6 |
| 52981366-e5e1-31bf-bdf8-509d05f64481 | -12.6186 | -44.6116 | 2026-07-31 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 01520354-a262-38bf-8a3b-5fc2978127ec | -12.6191 | -44.5882 | 2026-07-31 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| e0781014-24cb-3d6c-9cf3-264c86a8210d | -12.5993 | -44.6147 | 2026-07-31 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 317.1 |
| 09382e38-58c7-3560-a867-0d7cad2e32b4 | -12.58 | -44.6178 | 2026-07-31 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| dac587ad-d4ed-34d9-81de-760fb8fc7d26 | -12.5989 | -44.6381 | 2026-07-31 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 673271bc-6bd9-3719-b60b-b0aa94b0a191 | -14.1966 | -44.1029 | 2026-07-31 13:00:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 52fe5bd4-b091-363c-b212-acb3372648ac | -14.2162 | -44.0993 | 2026-07-31 13:00:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| de981f86-7001-3191-88e4-e36e2a804970 | -12.6186 | -44.6116 | 2026-07-31 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 248.9 |
| 8dafe62d-a361-33a8-8b15-120d00404e97 | -11.3178 | -50.3847 | 2026-07-31 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 53a73576-3e25-39b9-85cb-2445c8359cf7 | -12.6182 | -44.635 | 2026-07-31 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| bcb858cc-abad-3fb8-885b-153ec94caf78 | -11.3175 | -50.4061 | 2026-07-31 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 06c08b86-31b9-370f-ac3c-07489e6b8772 | -14.1966 | -44.1029 | 2026-07-31 13:10:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d378fd80-92ee-385b-98d7-c7d087e3cd4f | -14.2162 | -44.0993 | 2026-07-31 13:10:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| db8a16e3-685c-3f4f-80b2-f38e8efca22e | -12.6186 | -44.6116 | 2026-07-31 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 378.5 |
| fe4c9a35-f8fd-33fc-9afb-2b7e795b5ad9 | -12.5989 | -44.6381 | 2026-07-31 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| ce780509-bef5-31ca-b089-3c1dc43e6970 | -11.3 | -50.301 | 2026-07-31 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| e4b52ad6-9e05-3395-936a-e86fd4d23505 | -12.6191 | -44.5882 | 2026-07-31 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| c99bd82e-ec39-399f-a0eb-3a4114ee210b | -12.5993 | -44.6147 | 2026-07-31 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 466.2 |
| 89c113a9-f52d-306e-9d74-160bc35573fb | -12.58 | -44.6178 | 2026-07-31 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 67255c24-99c7-3d79-b885-a3628bd5b962 | 1.10193 | -60.51004 | 2026-07-31 13:14:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.4 |
| fed7cbd9-bea8-3c01-b225-499e2da855cf | -7.17533 | -62.80292 | 2026-07-31 13:18:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 89cc8844-ad53-3caa-b94e-0fd5c4cb884e | -12.6191 | -44.5882 | 2026-07-31 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 754937c3-471c-3357-bf69-8cedbaf6276e | -12.6182 | -44.635 | 2026-07-31 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 128f39ea-9629-3a14-b742-56911fa83986 | -14.2162 | -44.0993 | 2026-07-31 13:20:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| de1414b5-c978-3f9e-8f2d-207d535629f8 | -3.9959 | -43.2651 | 2026-07-31 13:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 125d1fb5-7365-369b-bc63-6a2c08b9a7c7 | -11.3178 | -50.3847 | 2026-07-31 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e229e725-d28e-3bd7-9ea1-0583ab69dc2c | -12.5989 | -44.6381 | 2026-07-31 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 164.6 |
| f46cfc36-d674-3631-a0d0-b504d7c3bbda | -11.3 | -50.301 | 2026-07-31 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| f36a5d6e-ad8b-33a2-91c0-f0ffab07ee57 | -12.5993 | -44.6147 | 2026-07-31 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 539.3 |
| 8e4ceae9-c36a-3941-9589-3232043c0048 | -14.1966 | -44.1029 | 2026-07-31 13:20:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 19aaad49-7f54-38c3-b0fb-d66522e42aa4 | -12.6186 | -44.6116 | 2026-07-31 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 358.0 |
| a60a134e-b04f-3ca0-ba34-eb2205e2763d | -12.5989 | -44.6381 | 2026-07-31 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| f47b9a43-ee23-3b7e-8473-2ab16e2f004e | -12.6182 | -44.635 | 2026-07-31 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| dce4437d-db6d-3897-902b-dcbcf788cfcd | -12.6186 | -44.6116 | 2026-07-31 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 368.8 |
| acb8ca0c-971c-3b1c-ad89-06a0e07061f6 | -11.3 | -50.301 | 2026-07-31 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 8cea30be-0f13-320f-8ca1-ddbd289068eb | -11.2997 | -50.3225 | 2026-07-31 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 7a85d8c1-17a0-3219-b0ef-b3510392b59b | -12.5993 | -44.6147 | 2026-07-31 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 480.6 |
| 0af75be2-5d58-3b0c-9f3e-dc86a033b850 | -12.6191 | -44.5882 | 2026-07-31 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 169.4 |
| a9ab380f-6466-3b0e-86cf-07d856391ab0 | -12.5993 | -44.6147 | 2026-07-31 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 442.4 |
| 111d6b7a-6e76-3515-bfb8-6f07835ed522 | -14.2162 | -44.0993 | 2026-07-31 13:40:00 | GOES-19 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| c1b6f361-dfcc-3af2-86cf-4a63589634eb | -12.6186 | -44.6116 | 2026-07-31 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 494.9 |
| 3e953797-01ca-3883-a2e6-e08cc317c0ee | -11.3175 | -50.4061 | 2026-07-31 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| e0196df5-474e-3308-94f3-b3d59d9f06d1 | -11.2997 | -50.3225 | 2026-07-31 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| a4494743-fbe1-3806-a8b3-ac2e83b12f0a | -12.5989 | -44.6381 | 2026-07-31 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 1ed45d0b-92f0-39c3-bb31-fc2424700387 | -17.0616 | -45.0191 | 2026-07-31 13:50:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 93750c11-94f0-3fe5-9d72-490c6bd6db23 | -12.6186 | -44.6116 | 2026-07-31 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 347.7 |
| 34759a0b-61e6-39e5-8609-954e44f9c2d6 | -6.897 | -43.5202 | 2026-07-31 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 76f7f38e-7cd3-338e-85d7-b2c680c368ff | -11.2997 | -50.3225 | 2026-07-31 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| a3f2713a-47e3-302a-aeac-ec9cc1895aec | -11.3175 | -50.4061 | 2026-07-31 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 6732a8b8-3714-3b11-a8e1-8fc337c75854 | -12.5989 | -44.6381 | 2026-07-31 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| ac6be542-6d18-33ed-8d52-58cc1810be35 | -12.5993 | -44.6147 | 2026-07-31 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 400.2 |
| bd9bfa5e-689a-364f-8165-920341320660 | -11.3175 | -50.4061 | 2026-07-31 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 1c2a6341-f3ad-39f6-9385-46141ca9f70f | -17.0616 | -45.0191 | 2026-07-31 14:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| cec64646-776f-3b7e-8508-dc0d9926bc75 | -11.3973 | -50.14 | 2026-07-31 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 80a34f3b-52ec-3c16-aaf6-d530e07f2a8e | -11.3175 | -50.4061 | 2026-07-31 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 21bebb11-ca12-3a0f-a35a-65cdb96a1829 | -17.0616 | -45.0191 | 2026-07-31 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| feb1f8a3-a57c-3e50-b642-7a0b5bc6578f | -11.3178 | -50.3847 | 2026-07-31 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 0a8573f7-a693-31a8-9318-0cc18830d6eb | -11.2997 | -50.3225 | 2026-07-31 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 90fb7d02-b8d9-3a58-90c5-86cfe6c67764 | -17.0616 | -45.0191 | 2026-07-31 14:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 2d0f4032-3084-3aec-9cfb-9ab602ad7f04 | -11.3 | -50.301 | 2026-07-31 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| d620c085-5af9-3fd7-ad90-9ddbf4f01d5d | -11.3175 | -50.4061 | 2026-07-31 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| cb9cd9e0-a91d-33c0-bed4-6c305ec0190a | -11.3973 | -50.14 | 2026-07-31 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d4679e97-6e98-3c83-9305-29f0716a7fd8 | -11.3175 | -50.4061 | 2026-07-31 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 239.2 |
| 9222da61-edb7-37cd-8414-71f958037b86 | -11.3973 | -50.14 | 2026-07-31 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 8a79d028-6544-30af-8b0f-8c85e8d1e32d | -17.0616 | -45.0191 | 2026-07-31 14:30:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0a717368-9776-3b63-8ed2-98cd9bca1af9 | -11.4163 | -50.1378 | 2026-07-31 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| a8ea9674-63e3-378f-a198-adce950dfcb0 | -11.3178 | -50.3847 | 2026-07-31 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 5033fd47-ceb8-396f-ac09-3ea9e788c041 | -11.3175 | -50.4061 | 2026-07-31 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| eb056cd0-01c6-380b-9b62-e710323a622e | -3.1158 | -47.9232 | 2026-07-31 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 02f2e240-2a66-323b-b134-7e0872149797 | -11.3973 | -50.14 | 2026-07-31 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 434cc8b7-f36a-3966-968d-7d9fcf0ef46a | -17.0616 | -45.0191 | 2026-07-31 14:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 99.9 |
| c9505e50-2739-3882-b957-6280f5c68978 | -12.6186 | -44.6116 | 2026-07-31 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 235.7 |
| 8a87492a-bcce-3d2d-92b2-327734422c58 | -3.1159 | -47.9015 | 2026-07-31 14:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0912a4cb-efc8-394b-b2c1-3bebff055b67 | -12.5989 | -44.6381 | 2026-07-31 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| ce2b4409-c29d-38a8-8faa-34cd7e5e420c | -11.2997 | -50.3225 | 2026-07-31 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 082976f3-3b98-3ecc-9d36-3c81d58700ad | -5.3016 | -43.649 | 2026-07-31 14:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 99692052-cbdf-356f-8f03-4c04d9ebbd5e | -11.4163 | -50.1378 | 2026-07-31 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 78b8df9e-86fb-39c6-af97-d4c772db7dba | -11.3973 | -50.14 | 2026-07-31 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c1b2cf96-f453-3e4c-93b9-c30ea03f6f29 | -12.5989 | -44.6381 | 2026-07-31 14:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| ca41978e-e8aa-3dbf-91e6-c5ed9c857e84 | -12.6186 | -44.6116 | 2026-07-31 14:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 230.0 |
| 672b7f70-8b9e-3506-9648-fd728c352bfc | -17.0616 | -45.0191 | 2026-07-31 15:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 53284c46-32e6-3f16-b6d0-dc76f3472dff | -11.9099 | -43.4556 | 2026-07-31 15:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 9b488631-2554-3613-ad80-5dafde167b40 | -11.9104 | -43.4319 | 2026-07-31 15:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 6ed20644-e24b-32f0-a2c6-57c7a04a1255 | -11.4163 | -50.1378 | 2026-07-31 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 1c154b7f-18ff-3537-8a9e-e2394d59cf53 | -11.2997 | -50.3225 | 2026-07-31 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.4 |


[Clique aqui para ver as próximas entradas](README17.md)
