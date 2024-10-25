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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbd987bb-8037-30a6-86eb-e38100314d15 | -10.87077 | -47.80534 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1130460c-2b06-38ed-92d4-fa41c96178b2 | -10.87018 | -47.80163 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 12313c4e-20ad-35aa-96d7-9380e5de6746 | -10.86679 | -47.80214 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 065c1e2e-915c-333a-94fd-de275f872b52 | -10.8662 | -47.79846 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 427b5cc1-3df7-3640-8782-e980cc99036d | -10.86339 | -47.80264 | 2024-10-25 16:50:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1961f348-fd3a-335c-8324-f225fd29b9ef | -10.82027 | -47.6418 | 2024-10-25 16:50:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eca7fcf5-cbfc-30db-a05a-d3efc9b5e0c5 | -11.43957 | -48.47912 | 2024-10-25 16:50:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 3a5c486b-b21c-3e64-b4d6-20486274bece | -11.43679 | -48.48322 | 2024-10-25 16:50:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 99cbec5d-c432-3ff0-baa8-bab9c2edab85 | -11.43624 | -48.47966 | 2024-10-25 16:50:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| c79ffd3d-8474-38d3-9850-591eff828ef9 | -11.37372 | -47.99252 | 2024-10-25 16:50:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb245af8-519a-32ce-bd7e-5e3869cebca1 | -12.17407 | -47.98286 | 2024-10-25 16:50:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 61ef6ac7-c1f3-343e-8bf0-cc911ce94611 | -12.17015 | -47.97981 | 2024-10-25 16:50:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 31c17561-e875-3540-bf79-5d187cd604ba | -12.14555 | -47.96884 | 2024-10-25 16:50:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6033631e-d725-356d-8d5b-00c5fa629032 | -12.14277 | -47.973 | 2024-10-25 16:50:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e36f6a9-53ab-3a0c-ad49-641826f086ed | -12.1422 | -47.96939 | 2024-10-25 16:50:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b2131f15-6e63-3e0f-8342-1dab6e14ba92 | -12.14163 | -47.96579 | 2024-10-25 16:50:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3025bf04-73a3-3d8f-a482-c5ee2b33cebf | -12.13885 | -47.96994 | 2024-10-25 16:50:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 651bb35a-19a3-3c97-a997-a1149603300d | -12.13828 | -47.96633 | 2024-10-25 16:50:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ed82351d-9391-3e54-908e-95a9fb6b751e | -11.47774 | -47.85159 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 344d3ab6-3eb8-35be-bfb4-7df7e4d310f8 | -11.42894 | -47.76175 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c26817d-9d66-3ea6-8397-79352ddfbbce | -11.33573 | -47.75128 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b59eed73-e6e6-35e8-8f23-a329ef65b444 | -11.3308 | -47.78594 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5df6ed5-5186-3c53-bcde-03ca406720d3 | -11.29513 | -47.75793 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 061a9ebc-ebbe-3e03-b40d-ce39904c7f98 | -11.29395 | -47.7505 | 2024-10-25 16:50:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| fb55f706-2752-3b18-aacc-51ced5b7a822 | -11.29175 | -47.7585 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| cca91bd4-73ac-33d9-b9c2-c26a7248e883 | -11.29116 | -47.75476 | 2024-10-25 16:50:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 9b60fedf-123f-3fc3-a2fa-370f16840977 | -11.17361 | -47.72149 | 2024-10-25 16:50:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7cff8822-f629-3b04-815e-c2f09b2bf0af | -16.31546 | -49.53886 | 2024-10-25 16:50:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eb0cc109-11d6-3cd9-95eb-ec9548176dfc | -16.29848 | -49.46971 | 2024-10-25 16:50:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e0aac4a-ce75-363c-b426-ba5f8beb190f | -16.28456 | -48.91551 | 2024-10-25 16:50:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 79f4f731-6099-3c57-842d-24c7178680e6 | -18.31 | -56.17589 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.2 |
| f9afb21b-3de0-3a80-b349-d6e221280c46 | -10.84628 | -49.54585 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 32bcb2d8-3a5b-30ce-aef6-b8a0a0dfe75a | -10.84574 | -49.54235 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 29afda87-7fbb-3380-884c-07a318ca5e1a | -10.8435 | -49.54986 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 041bbf6b-84ee-31d6-bb42-56bc37cf5e1a | -10.84297 | -49.54636 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 86aaabd5-c031-3280-b14a-6ddebda31dd9 | -10.84243 | -49.54287 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ebed27e5-97ae-3eea-8f85-e62276cfe19b | -10.8402 | -49.55038 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d842e3e7-1792-369f-901f-108ee3d1fa63 | -10.83966 | -49.54688 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e3eaed6d-e5ea-39a7-b0a4-8cc323773b32 | -10.83913 | -49.54338 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f0664295-45cb-350b-8a93-8d82c0e7f3a0 | -10.75799 | -49.14778 | 2024-10-25 16:50:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| ed4b97c5-e85b-3f2b-b3a6-fd735b03e7a4 | -10.68454 | -49.53191 | 2024-10-25 16:50:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ef194b52-0e8f-3434-baef-5a4682087e79 | -10.10184 | -49.10358 | 2024-10-25 16:50:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20a9504b-88fc-3d43-91d2-e4b77a2da388 | -9.98435 | -49.3767 | 2024-10-25 16:50:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f944f416-f422-33a3-86f5-15073a67b943 | -9.88908 | -49.11279 | 2024-10-25 16:50:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9dac1b3-bcd3-3db9-a8c0-2545e3311d33 | -9.78737 | -49.31258 | 2024-10-25 16:50:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 580149e1-1a50-3597-9017-bb8c3bf4ca01 | -9.88224 | -49.90837 | 2024-10-25 16:50:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a77c9df7-a184-3383-84ec-b5e09677e4cc | -9.88171 | -49.90488 | 2024-10-25 16:50:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 36e89bcb-42b7-3349-a042-f90a7144008d | -9.88 | -49.91586 | 2024-10-25 16:50:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d837f925-6feb-33d2-bfdb-bd314f60df8d | -9.87947 | -49.91238 | 2024-10-25 16:50:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3b4fdef-3f90-3054-a24c-054b132cd310 | -9.8784 | -49.9054 | 2024-10-25 16:50:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f1236df3-ce94-3b4c-adcd-ccf140fc5731 | -9.87787 | -49.90191 | 2024-10-25 16:50:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bd87528f-f393-3079-8723-7f8bcf5d4fa3 | -9.87509 | -49.90591 | 2024-10-25 16:50:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ddfb2501-e849-3b17-8579-88d71f9b89de | -9.868 | -49.99274 | 2024-10-25 16:50:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e17184ac-bc45-329b-b629-e3cde649e768 | -11.06345 | -49.63218 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f30dabce-8c9f-3ed5-9c4d-87429993e370 | -11.06291 | -49.62868 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fa4ba21f-4f99-3362-9cc8-5c9a2348c48a | -11.06014 | -49.6327 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3c0a2d52-5aa2-3b62-ae3c-3ddda1153b26 | -11.05961 | -49.6292 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3430ec39-80b8-3bff-b548-2a45ac8d595b | -10.97838 | -49.2979 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8edb978f-89cc-3baf-88e8-a080ebb9458b | -12.4758 | -49.9192 | 2024-10-25 16:50:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3d1e2d60-69ee-313d-8950-139e0a8c836d | -12.30546 | -50.27982 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f93a19aa-aad8-3f61-bde1-1ba981562a95 | -16.49665 | -51.27607 | 2024-10-25 16:50:00 | NOAA-21 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c2b981ec-370e-3ef0-b375-9c66f639b174 | -10.73989 | -51.75416 | 2024-10-25 16:50:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 859d9a61-5905-38fb-89a1-19ca1430d195 | -10.73932 | -51.75032 | 2024-10-25 16:50:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 74353c7e-dd54-3b74-8be1-8a07a38adc26 | -10.35293 | -51.20227 | 2024-10-25 16:50:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aa8c745c-02e3-3254-be39-b66d19527d18 | -10.10002 | -51.12566 | 2024-10-25 16:50:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| befca218-8442-32ab-b6a6-29a6d6cd3ea2 | -11.55488 | -51.39165 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 72a98cba-0ebc-3a5c-bf81-818f07219659 | -11.55432 | -51.38786 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| eec9e6bd-ff41-3c9f-a08e-15020404d787 | -11.49894 | -51.46613 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 025b455d-90fe-3047-8fc0-ad69c807187a | -11.37202 | -51.29172 | 2024-10-25 16:50:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7d6bcd70-08ec-31a2-a66f-6cbce32dda40 | -11.02355 | -51.49387 | 2024-10-25 16:50:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6d35a13a-9afc-34f3-9f8d-785db254c801 | -12.37658 | -51.09848 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 706b7db3-32d6-30c5-b750-1530d62bf407 | -12.28193 | -51.02762 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0855b35a-f3db-3c68-878d-491a5850f801 | -12.22707 | -51.08204 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebbdaf29-20be-328e-bbb2-248cf40a29f4 | -12.22421 | -51.08632 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ebbfc7e-7157-3231-b465-079136f285a3 | -12.22366 | -51.08255 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 300c6841-d1a3-34af-800a-7a7253bbb019 | -12.21737 | -51.08735 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ce78b73b-df16-35b0-85e8-3fa7e0fc06ab | -12.18619 | -51.0651 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aad3e878-d9ef-3987-a0f4-e8d792de337b | -12.18202 | -51.0621 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b7ecc4aa-f31d-3d92-b438-41113dc18324 | -12.17805 | -51.05886 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8669daec-cda1-329a-8302-ad28bc2f236c | -12.17463 | -51.05937 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 08df4e88-bcf1-34d9-93a5-d1cf8cae090a | -12.17408 | -51.05561 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 04b847e3-c188-377e-b4a4-9a1b4c7b3894 | -12.17185 | -51.0406 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7566c92e-3f33-3ff5-b5f6-453f631a0373 | -12.17122 | -51.05989 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cc4f9e42-f0db-3c1e-a298-92c6c37f7b8e | -12.169 | -51.04486 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3619e9a4-9d2d-3e43-9f14-eff0c73ccb5f | -12.1678 | -51.0604 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6814d894-244d-3814-b1ff-368da9d0bc0f | -12.16725 | -51.05664 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 88e7e0dd-a350-3a83-a55b-e44d58ab9708 | -12.16669 | -51.05289 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 31e04c39-eab6-3335-a7cf-dd440afeba59 | -12.16384 | -51.05716 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a2a62b5-84cb-33bc-a792-d2004a421a9c | -12.1452 | -51.02544 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a3b9017c-8b97-3de3-885d-3ef2515e367d | -12.14124 | -51.02221 | 2024-10-25 16:50:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8f9647f-f511-3116-a2cb-5a60c923348a | -15.52834 | -52.66755 | 2024-10-25 16:50:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 167e7974-8610-3ccd-b8f1-7a394d7cdb93 | -14.31546 | -53.98546 | 2024-10-25 16:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7179f7d0-8bae-37a4-8855-f79501118336 | -14.10196 | -54.28366 | 2024-10-25 16:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4950c240-8933-358f-9139-6d4be6188e68 | -16.07993 | -53.75002 | 2024-10-25 16:50:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2740e2e-5f64-3a37-bcbe-823e590aa93c | -15.72753 | -53.37207 | 2024-10-25 16:50:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 478a93c8-37d9-3652-961c-0a91eae39e7f | -16.77648 | -53.62799 | 2024-10-25 16:50:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8c5fc744-2907-36a0-995a-0426ffaf9ba3 | -10.84108 | -54.09417 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f817bf0c-e6aa-3301-b467-321a8b076359 | -10.83717 | -54.09475 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 628c27fa-fc5a-32ae-a2da-55e3b3ae2bd1 | -10.79694 | -53.86386 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 166.3 |
| 3d562dc6-830b-3a27-9afe-69544715169b | -10.79625 | -53.85897 | 2024-10-25 16:50:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |


[Clique aqui para ver as próximas entradas](README133.md)
