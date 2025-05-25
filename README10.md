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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eba18e10-a27e-30bb-b419-3d5ca97441de | -14.06416 | -57.11419 | 2025-05-25 05:08:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0399cc61-4e3d-3bda-a4e6-16295951eac8 | -11.42511 | -54.3161 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7394de4-16b8-34d9-9a88-fac0bfac43fe | -17.15367 | -54.00532 | 2025-05-25 05:08:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dd4c7bb-e4ab-3804-9d63-3d8ffababa3a | -11.75432 | -54.22924 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c62e6ad0-de65-3a94-8142-8090b7c051b8 | -14.03773 | -55.13181 | 2025-05-25 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 09a4435d-6dd4-3849-b586-d176b572adc2 | -12.35535 | -55.43542 | 2025-05-25 05:08:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ca73a79-7c15-3bf1-9dfb-8bacfaf499a4 | -14.02953 | -55.13874 | 2025-05-25 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99c69ecb-368a-3135-926c-575eb3bbd4ce | -14.68737 | -52.68494 | 2025-05-25 05:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94b9656b-6dfc-3f02-9d35-f20fe4386f28 | -13.14274 | -56.80467 | 2025-05-25 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfe4e040-0f5f-3805-9b7a-7cce6e6654bf | -14.02018 | -55.12908 | 2025-05-25 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ddb964a-34c8-33db-9bce-74fe28a6ebbe | -11.39872 | -52.95447 | 2025-05-25 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c582b3f-b874-3bc4-bfd5-f24cc7cf7803 | -12.37095 | -54.89829 | 2025-05-25 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ba47413-f6d4-38f7-8aca-aa870137e5d4 | -13.08763 | -54.86819 | 2025-05-25 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f72c85a0-669e-3ced-80c5-dcdbb2cb38b3 | -12.25657 | -56.5863 | 2025-05-25 05:08:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08c4076c-bb36-35d2-8d3f-24d9214422a5 | -11.99058 | -57.20787 | 2025-05-25 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dad3b64-b010-3273-bc27-a55dc2f2ae02 | -12.25936 | -56.59039 | 2025-05-25 05:08:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 412580c2-cf77-342a-b46f-360315c8fabc | -12.67415 | -58.22144 | 2025-05-25 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bc49b27-5be0-3188-b4cf-6ad639b86f45 | -11.73755 | -62.72607 | 2025-05-25 05:08:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9392d77-b0af-34f6-bd05-6fbb1194f161 | -12.66745 | -58.2203 | 2025-05-25 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7560c1d-c6d4-36ac-ac91-ed719c3bfa19 | -11.30715 | -54.02503 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d12de016-974a-3679-8c02-e4c5df1f17b6 | -11.74173 | -62.72689 | 2025-05-25 05:08:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcb84f69-9fc9-3812-85c6-3674324d93cd | -12.13719 | -54.65825 | 2025-05-25 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d44d65f-a06e-374f-a14b-7d5d38632539 | -12.6708 | -58.22087 | 2025-05-25 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56e3ce49-7934-322f-9d7b-a25a2621a396 | -12.37725 | -49.9887 | 2025-05-25 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a180e07c-fc51-30da-b99a-92147c91591e | -11.86823 | -52.25408 | 2025-05-25 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac3f3144-ea4b-3fae-b254-ed9ca46bfec7 | -11.9151 | -54.41103 | 2025-05-25 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 040eccae-80f0-3f36-8686-6346d5054f1c | -13.15498 | -56.81398 | 2025-05-25 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a720aa4-94f6-3826-ba8e-6d1d1a2453c2 | -11.29894 | -53.98145 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a246cdb-e6b5-3e5b-883a-359d9e271cf4 | -11.42629 | -54.33271 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b02f2d11-5afc-3303-91f9-bf669f10be3a | -11.42157 | -54.31555 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98964d8e-8479-3f3c-bac9-0d9e81b05717 | -11.75372 | -54.23332 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e11b1303-7c8b-3aca-ba6c-90ba5e7303b3 | -15.0792 | -48.94388 | 2025-05-25 05:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4c07569-c0ee-3a02-93ac-dc15223355d8 | -14.20335 | -60.05061 | 2025-05-25 05:08:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86360f79-5960-3a9d-9e9a-38ee3c85e95d | -11.42983 | -54.33325 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5e15ae76-ea3e-3482-b70e-70d043b2aab6 | -11.36433 | -55.12544 | 2025-05-25 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1c165d5-7715-3c90-ba76-ba534301f42d | -12.37386 | -54.90273 | 2025-05-25 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38945df4-f782-3e85-a977-84eff8e314a0 | -11.74658 | -54.23227 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 149bafa2-4cf4-3f89-9c1a-378731c90377 | -17.61511 | -54.17661 | 2025-05-25 05:08:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffcd0cd6-d8c8-3b0f-916f-66cf4bc1ce74 | -13.14608 | -56.80521 | 2025-05-25 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8d751f4-94a1-3192-9d01-608040d58588 | -11.29535 | -53.98089 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e79122e-8f9d-3751-b388-a062e32d2bec | -14.20684 | -60.05124 | 2025-05-25 05:08:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57561166-d728-3224-81f5-2176a8e48459 | -14.67929 | -52.68375 | 2025-05-25 05:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11a66809-6ea0-30ed-80f3-c525da1b4a35 | -12.13952 | -54.66677 | 2025-05-25 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98b52221-175f-358e-b4df-46cb5f8d5416 | -15.62896 | -57.3076 | 2025-05-25 05:08:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2a65aa8-bde7-33c1-bf94-371ea2547e77 | -11.42688 | -54.32871 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56e0efa3-db70-3ee1-826e-18499c91df28 | -14.03422 | -55.13128 | 2025-05-25 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67698d0d-b973-3115-9fa5-cb830cb4ef47 | -12.66803 | -58.21671 | 2025-05-25 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08455084-cd17-3e59-a59e-20ef265d8ca0 | -11.99391 | -57.20842 | 2025-05-25 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c56d60e3-066b-39e4-a395-0d22ad427c67 | -11.99335 | -57.21195 | 2025-05-25 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eeecbf58-d917-32d9-a06b-73b8e390a932 | -14.67881 | -52.68737 | 2025-05-25 05:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4f170ff-baa3-35e7-9b52-df5f4eee0588 | -14.03071 | -55.13074 | 2025-05-25 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7daa4be2-1f30-3637-a129-d1fd001af2b9 | -11.30417 | -54.02038 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6f5d534-6c9c-38d3-894a-3a79363bb8a6 | -11.99668 | -57.21249 | 2025-05-25 05:08:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a07d19b6-5460-3a71-a33b-2a171a6c2254 | -17.61893 | -54.1773 | 2025-05-25 05:08:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4d189ee-ef11-3e34-831a-2bcac8095131 | -11.36033 | -55.12866 | 2025-05-25 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d7e9e3a-a927-3861-9c46-2b3daecfa779 | -11.30654 | -54.02913 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 617902a5-4183-3f7a-80fc-9536df9b0604 | -13.9846 | -56.02045 | 2025-05-25 05:08:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07c0545b-70f5-3120-a600-14543b45d19d | -14.01667 | -55.12854 | 2025-05-25 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4b5092d-a69d-3ad0-8a1d-2941e464ce71 | -14.02193 | -55.14163 | 2025-05-25 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51d21058-84f2-32c8-aff2-a79108950760 | -13.15443 | -56.81755 | 2025-05-25 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9a26e28-42d8-3e9d-9583-8600072951aa | -11.4664 | -61.93991 | 2025-05-25 05:08:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 743c15e2-d0bf-3324-9c91-4a105894f6e7 | -11.29833 | -53.98557 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb867597-3ef8-36b5-9666-3eb88e8706aa | -14.46945 | -56.31958 | 2025-05-25 05:08:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8fa8a41-2780-39f1-9e53-dfc4014db8dc | -14.02661 | -55.13419 | 2025-05-25 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 307cafbe-6b84-3fac-8625-8a038ec3ec9f | -14.68333 | -52.68434 | 2025-05-25 05:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe7f2ecd-388b-34a0-a161-d618f798824f | -11.36491 | -55.12169 | 2025-05-25 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f392bc3-aade-3b3f-b2a5-d7de78f77f0e | -11.29474 | -53.98501 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0345addc-e611-3a56-821e-37646046ed24 | -13.7521 | -58.59369 | 2025-05-25 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a86ebc1-e349-3412-bb05-c94f3cc56411 | -14.20402 | -60.04666 | 2025-05-25 05:08:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad08a327-2876-3f4c-ac83-fee300560a24 | -12.25991 | -56.58684 | 2025-05-25 05:08:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0f9347b-ce0e-3257-8842-a663b33631ce | -15.07878 | -48.94738 | 2025-05-25 05:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e318409e-0b11-31fd-ba4d-35e8c96f2554 | -14.02602 | -55.13818 | 2025-05-25 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2377016-7514-3b0d-b4a6-0c7d23935519 | -11.30356 | -54.02448 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83e9d816-5846-3fff-b07a-e0ffc9ad8227 | -14.03655 | -55.13981 | 2025-05-25 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7978f792-c33f-3c96-b994-76b3bdb92ff5 | -13.09898 | -52.2865 | 2025-05-25 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c21c4fc-fd7b-3c17-a81f-e7ac546edf9d | -13.15276 | -56.80629 | 2025-05-25 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc59d036-1507-3875-91e0-2228a0860319 | -13.08822 | -54.86419 | 2025-05-25 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ba8c9b5-a552-3bc1-bc3c-f2da0a59fc1d | -11.86749 | -52.25928 | 2025-05-25 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44337b83-de11-3998-9ebe-931f339e6bac | -12.50052 | -55.18962 | 2025-05-25 05:08:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dadd9f1e-a480-3f1f-a9d0-4edb3e8b9123 | -13.36324 | -56.71125 | 2025-05-25 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32f584af-c470-3fe7-9166-64b572eac83a | -14.68382 | -52.68071 | 2025-05-25 05:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71b43eb0-a514-37b9-9637-b47843b69da2 | -11.75015 | -54.23279 | 2025-05-25 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74edc073-86df-390c-83c1-d77208242dc6 | -14.04007 | -55.14032 | 2025-05-25 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfc10e1d-11d2-3657-8a96-22e67c9046f7 | -13.1522 | -56.80986 | 2025-05-25 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3958dcc6-5d38-3d2a-b6df-5877eb24fa85 | -12.37195 | -49.9929 | 2025-05-25 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db80631a-f163-3edd-b0d6-b7ddbf440d90 | -11.82744 | -55.21746 | 2025-05-25 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 26ff4e49-e293-36a2-8457-a3619e3d526b | -14.47283 | -56.32013 | 2025-05-25 05:08:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88eb70e5-705e-393f-a6aa-6dd6a509f09b | -7.6574 | -46.1013 | 2025-05-25 05:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| a824be5f-066d-3603-9d6c-0a11deb9f02d | -19.87522 | -54.36938 | 2025-05-25 05:10:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0fdd53e7-52a0-3934-9cf4-aa2d330e485a | -20.51576 | -51.41763 | 2025-05-25 05:10:00 | NPP-375D | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5ec94266-254d-3be0-940a-3f063cdd3bb6 | -20.94045 | -56.59238 | 2025-05-25 05:10:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b87039ef-118f-3f06-b6aa-7ad09188d187 | -21.62612 | -49.78099 | 2025-05-25 05:10:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 01324cc5-ea95-306e-a044-58b9c083035f | -23.24109 | -52.34491 | 2025-05-25 05:10:00 | NPP-375D | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 1da1fee8-d5e7-3864-ab42-1fc5e0f925fb | -20.70435 | -50.06636 | 2025-05-25 05:10:00 | NPP-375D | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 11cb1d18-be21-32ca-a236-9db58a817cdc | -21.63147 | -49.78175 | 2025-05-25 05:10:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8edcfb84-d62b-3a11-ac68-ec7c561d9ede | -20.52051 | -51.41824 | 2025-05-25 05:10:00 | NPP-375D | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| afe7d5de-37cb-3325-ac67-f3c4c85bd3fa | -21.1847 | -53.1804 | 2025-05-25 05:10:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb92d0b1-b4bf-3d3e-9509-a0ac2a30c048 | -20.94338 | -56.59711 | 2025-05-25 05:10:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0bac8659-405a-3bf1-8909-5534b371b235 | -23.98519 | -48.91924 | 2025-05-25 05:10:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9013dde-8373-3c98-83ba-cf6b80fd3b5e | -20.93986 | -56.59653 | 2025-05-25 05:10:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README11.md)
