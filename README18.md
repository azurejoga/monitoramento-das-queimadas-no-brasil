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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32f3b03c-8e16-3e92-a510-76b077111eb5 | -15.36504 | -42.20063 | 2026-09-16 03:55:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e4320027-c30e-319a-b59c-e03826623a2c | -10.59021 | -47.75174 | 2026-09-16 03:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04200cbc-b571-3e05-8b76-0da73676858d | -12.70964 | -45.61804 | 2026-09-16 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f356215e-e339-3c46-8c9a-f9943b26f8d8 | -9.23642 | -46.69984 | 2026-09-16 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07049d4a-fe7a-3c7b-b397-4ebc38d88c69 | -10.595 | -47.75273 | 2026-09-16 03:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91b77c45-aa0b-3bc9-84f7-d289afca45cf | -9.09377 | -45.7293 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4e6c6ed1-2ac3-3f2d-8b25-64c6620bd734 | -9.54831 | -45.41769 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a348e4fa-859e-3651-bc8a-6cc215a126df | -9.76042 | -46.58559 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a1511acd-7714-3de8-91c4-2ce7187e72f9 | -12.32878 | -47.96301 | 2026-09-16 03:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4f6ff906-52d3-366a-980b-72359d5af3ca | -8.85662 | -44.90487 | 2026-09-16 03:55:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75fb58ec-9a95-38e6-a639-1bc379387fc3 | -15.03148 | -41.46088 | 2026-09-16 03:55:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4d30542-a984-3a2d-9911-fdd69533fa56 | -9.84297 | -48.35545 | 2026-09-16 03:55:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 388e5925-de00-3a65-86b0-5a9036f300ec | -15.28169 | -42.814 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd40b624-adac-3ffa-b8ae-0860a9935a8e | -14.66757 | -48.02126 | 2026-09-16 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 378bbd3c-8514-3ae9-8ef5-9d4d8ed6cc92 | -9.11544 | -45.73691 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 44861200-d6f1-3d13-9edf-6d3b6438f808 | -15.29799 | -42.79502 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89319a1b-2d37-3bec-83b9-0ebba8d9f58b | -9.78415 | -46.55149 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 579551e3-c91e-309b-b39e-a1d2095b54ab | -11.55141 | -46.86315 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c86179af-ada5-3a70-bfbe-3a85ae69e254 | -12.32274 | -47.96164 | 2026-09-16 03:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f29c9bc5-59b2-3bd6-a81d-7d7967068dac | -13.64717 | -45.96089 | 2026-09-16 03:55:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86f8cec0-bffa-36b6-819f-fb2553630aa0 | -10.82197 | -46.17736 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9122b0d3-d604-3bb8-958e-8841cb485c72 | -9.7619 | -46.57774 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c061020b-e4f3-3443-a184-52a4837a9888 | -10.09985 | -45.61932 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfc45291-37df-3e28-83c1-06f4b6b1bb96 | -10.8247 | -46.18019 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbd5d772-1b97-37c9-a25f-4fabd633eff3 | -14.22733 | -48.51297 | 2026-09-16 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e072903-da78-348a-a983-f05d4dd9e86a | -11.5406 | -46.85735 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 460a28ca-6f54-30c9-86cd-18405e4dd907 | -10.09904 | -45.56434 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99bcfa40-6737-33e6-a5d5-b842fcd94144 | -12.64026 | -40.90513 | 2026-09-16 03:55:00 | NPP-375D | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ff154456-9ec2-3a09-b31b-9b3bf58602a0 | -11.89381 | -43.82558 | 2026-09-16 03:55:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| e3f77029-d380-3113-9dd5-69c8ef2129da | -15.29404 | -42.79329 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d8ffbd0-9be0-3d18-943d-b0b595e191e7 | -11.88821 | -43.82972 | 2026-09-16 03:55:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 34ae937e-df4f-3bab-b055-3702621598b4 | -9.10074 | -45.72293 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da870d77-8c2c-348e-a013-694e545c5277 | -10.10068 | -45.61495 | 2026-09-16 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5a34a35-11c0-3ca7-be18-67288689590b | -13.29342 | -51.27902 | 2026-09-16 03:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe6ecaa4-fd53-3d71-b93b-6def87965360 | -10.75677 | -44.81611 | 2026-09-16 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69732190-57de-3c81-935e-aee5fbe53b5f | -13.6335 | -45.97539 | 2026-09-16 03:55:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac243b05-0730-39a3-80ea-ad86c17a5cf4 | -9.09516 | -45.72194 | 2026-09-16 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45ea408d-170e-3a8c-bdd0-122a7a186c9b | -12.5375 | -47.10815 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 36984306-dd5d-3e77-8f0c-616ed3a2d7b4 | -10.81913 | -46.1791 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 591f8e96-295d-31e9-bbb0-f0b1eaf0f50e | -13.55049 | -43.50729 | 2026-09-16 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08025fd4-3054-3f68-a003-0c225f4b7511 | -15.88825 | -40.2226 | 2026-09-16 03:55:00 | NPP-375D | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d6df812d-413d-39d3-95f9-ae45364e57d0 | -9.79048 | -46.4897 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a446703d-c566-357d-91b6-cd595074b96e | -12.71745 | -43.20354 | 2026-09-16 03:55:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dfd6d626-ab73-37c7-b32c-162a0e941ae2 | -12.46923 | -41.39896 | 2026-09-16 03:55:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 16.7 |
| c547db5e-dedf-3bef-9844-31e539e93c97 | -15.35694 | -48.1102 | 2026-09-16 03:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf788ba4-3249-3945-9782-983de48e84e2 | -9.79043 | -46.48835 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8af4bf3c-5aa0-36d9-8d70-5b3d0ae51cf4 | -11.55165 | -46.86108 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 063aeddf-aab1-360e-b875-53b733e968ea | -9.81298 | -48.91273 | 2026-09-16 03:55:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29d8d7a5-4b97-3434-afaf-bbe7b8f73f04 | -11.16732 | -42.80483 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3055630d-4b3b-3bd0-bf4a-fe9abd1cce71 | -12.53586 | -47.11639 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 46730dfd-e3f1-3974-88f7-e4a23eaf2383 | -11.2488 | -43.43975 | 2026-09-16 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf1cac5c-2ad8-36c0-bc50-e048ced223a0 | -10.83167 | -46.20378 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f564a951-9cb0-37a1-88ef-43453c827b1d | -11.1814 | -42.80291 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e5d7b2f6-35cb-3e70-bdb9-6a8b0d61b9e1 | -8.85722 | -44.90157 | 2026-09-16 03:55:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1900cc5-1504-3205-9c8d-02fc3e296aca | -11.55068 | -46.86697 | 2026-09-16 03:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b6b856b5-5545-3bc4-9e5e-b7433bb97c84 | -9.23052 | -46.6986 | 2026-09-16 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fdd977b-bc15-3370-90c3-12eea894278c | -10.75357 | -44.81779 | 2026-09-16 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b4be4bf-62b3-301c-b85c-2614d1e68026 | -14.86091 | -49.97211 | 2026-09-16 03:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d2098f6e-3d2a-3045-8e6d-0c01e1089e6a | -10.40052 | -48.64418 | 2026-09-16 03:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 608591e0-2325-3e5c-98d8-5154ff719e8e | -11.26064 | -46.5733 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0cf040f4-beb0-3cfc-b6a8-1ebf97a70108 | -8.64768 | -44.45487 | 2026-09-16 03:55:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a7df2a1-c73c-3463-a9b2-dbabc37c55ff | -13.55608 | -43.52701 | 2026-09-16 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61770c0e-9f30-3a63-8025-dd4111b34e84 | -14.85843 | -49.97615 | 2026-09-16 03:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f12bc0c3-7efb-3e18-b54b-8364ff7930a5 | -10.59919 | -47.76374 | 2026-09-16 03:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9aae7155-9e21-3f91-9aff-53da6dc87d2e | -9.54226 | -45.42006 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39f4bde1-c974-33d0-92a3-e0d20c6e20df | -15.17385 | -43.8489 | 2026-09-16 03:55:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c50d04bb-8ea3-380f-b006-923dd2c01a8a | -10.45848 | -44.94697 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fac937a-cbbd-36d0-87aa-7d311ebda308 | -9.48887 | -45.435 | 2026-09-16 03:55:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a281bf0-e7f4-3f21-8a44-be5ed77703a0 | -12.54977 | -47.10635 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d8e50d9-2361-3bc8-abd8-e80e4ce5cd83 | -11.19959 | -42.82915 | 2026-09-16 03:55:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5aac7294-9259-310e-9271-289ceb70c1a0 | -11.31638 | -47.23767 | 2026-09-16 03:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00f22792-44a5-3831-beed-67aa7097ff82 | -9.81176 | -48.91884 | 2026-09-16 03:55:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1546777-fd2e-3c30-8a1f-987ce4ecb2aa | -11.34141 | -47.3133 | 2026-09-16 03:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82969242-5d8a-3dbe-afed-a3081d937bc6 | -11.99448 | -43.78547 | 2026-09-16 03:55:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29e78a84-8705-338a-9876-a61f7423ea21 | -9.79978 | -46.5041 | 2026-09-16 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 719fa15b-b98c-3827-ad59-735b0d991a10 | -12.3297 | -47.95848 | 2026-09-16 03:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 792c0ffd-863a-386c-8725-ffe4b9390bd5 | -10.84944 | -46.17184 | 2026-09-16 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc496816-355f-36a5-a9d0-dcf86ecdcd03 | -11.24164 | -43.47847 | 2026-09-16 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ce59b32-da4e-3247-a3c0-f7ad05e7348f | -14.39793 | -44.70683 | 2026-09-16 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90b48bdc-723c-3ec0-9ed1-e23bd993c07a | -9.57297 | -46.59494 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfda355e-d6dc-3dd5-8032-24e0e9cfa48b | -15.35113 | -48.10905 | 2026-09-16 03:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 978c6ddb-b5de-309e-a552-7f6a4adcc1d9 | -9.76618 | -46.58176 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ea3df4c2-c773-39c8-8721-75e6614e237e | -9.56909 | -46.59132 | 2026-09-16 03:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af65c377-d559-35e3-93ac-a04da40e8582 | -15.28642 | -42.81149 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae39083b-f79b-36fd-8eee-d2fe3b010899 | -15.2798 | -42.80107 | 2026-09-16 03:55:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf51deb9-6716-3d9c-b75d-7879f4442b5a | -14.60695 | -42.14582 | 2026-09-16 03:55:00 | NPP-375D | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e8568ec2-d681-3219-9e13-062450830f2b | -12.5203 | -47.10465 | 2026-09-16 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b44ae63-2b73-3382-bf0a-5138a63130a9 | -12.15793 | -47.99261 | 2026-09-16 03:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcd3a487-7428-3b89-812e-6879569679a3 | -10.5954 | -47.75797 | 2026-09-16 03:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e39acf69-0be1-3f0f-83fe-8c2141d0b392 | -11.97723 | -44.93034 | 2026-09-16 03:55:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a49d755-3cbf-3751-8a00-c4fe77bba975 | -9.22968 | -46.70295 | 2026-09-16 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b243a22-de74-3420-9984-1ae260e38866 | -11.13451 | -40.47679 | 2026-09-16 03:55:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 073db9c6-992d-3d54-b5a0-b09426ddfbf3 | -8.85059 | -44.90779 | 2026-09-16 03:55:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b37494a9-d665-3fae-9779-f5f2e30e3285 | -12.47456 | -41.41488 | 2026-09-16 03:55:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a5447276-4354-3525-ab3b-e3f2d33a473a | -13.56053 | -43.5279 | 2026-09-16 03:55:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9bef040b-4e88-3c8c-9549-20a828fbd155 | -10.41299 | -48.64335 | 2026-09-16 03:55:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d80400ff-d941-3720-9f22-6d06f8220162 | -13.34715 | -46.30907 | 2026-09-16 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a141c206-bc6f-3503-9d3f-7d3320a9f2a0 | -10.59406 | -47.75734 | 2026-09-16 03:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7678698c-7583-3359-8a7d-125dddfba0d4 | -11.24419 | -43.43887 | 2026-09-16 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ecbc177-7d5a-32a4-b515-637d556239cd | -10.46425 | -44.94474 | 2026-09-16 03:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README19.md)
