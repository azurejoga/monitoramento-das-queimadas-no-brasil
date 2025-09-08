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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 664c145e-ba4d-326b-978e-53d8d0b79dd0 | -8.7279 | -46.685501 | 2025-09-08 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb6208b7-0101-3e9d-922c-1ffbe6754dbf | -9.9417 | -51.195599 | 2025-09-08 00:25:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c0d84f8-f932-3fad-9285-9ba3086bf467 | -5.5007 | -44.913601 | 2025-09-08 00:25:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 625e2e4e-dec4-3122-868b-bfcd62f1092a | -15.7401 | -53.564499 | 2025-09-08 00:25:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f95e82cc-6645-33de-ab0a-8196ca5b5bd7 | -5.6311 | -45.1241 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 400c4ed5-6fa2-3472-ad74-d100b8f5210c | -13.6797 | -45.484299 | 2025-09-08 00:25:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1239970-cd2c-3924-b00b-e6a7559e86e1 | -16.5319 | -45.118301 | 2025-09-08 00:25:00 | METOP-C | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b14139f2-bdc2-39a6-8d58-ec793c6990d9 | -10.802 | -47.746498 | 2025-09-08 00:25:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fd9ac8f-40f7-3c62-9866-7cf749372649 | -11.3951 | -43.5947 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fe8ecd9-8aef-3670-bd3e-d88db540d468 | -11.2648 | -46.461899 | 2025-09-08 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a4d8f3e4-4f05-3d6b-bccf-ab6a48ee930c | -11.6057 | -47.1465 | 2025-09-08 00:25:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 265a98e8-fd65-3c71-8c0e-11798e54389c | -7.0648 | -43.9063 | 2025-09-08 00:25:00 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 216ec8e2-9b66-3b60-911a-98b63fb1f9ca | -13.7963 | -46.277901 | 2025-09-08 00:25:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3accd88e-f8df-3d41-8fa4-91d10f15a906 | -5.7683 | -44.9118 | 2025-09-08 00:25:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f6a89f3-2c89-3655-bc5c-f538b9a9a62a | -7.5568 | -44.6647 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a579ee36-35e5-3d21-ad0c-d98c316a6b99 | -6.3638 | -42.608898 | 2025-09-08 00:25:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ed89335-0a77-3140-99e6-62312ee1e6c5 | -6.4462 | -43.952301 | 2025-09-08 00:25:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c3804dd-1609-3b76-b953-f16a7544bdf0 | -7.1237 | -44.572201 | 2025-09-08 00:25:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c508f81-f8f7-3574-b110-0ba6238ec1d8 | -6.2214 | -43.511902 | 2025-09-08 00:25:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 901c8686-1482-39d6-9aac-e468d6478161 | -5.863 | -46.103001 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a095ee9-aa93-3db1-be3a-65214429145d | -9.1866 | -46.062302 | 2025-09-08 00:25:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b987b7f-dc9e-376f-933e-59533b0ea852 | -13.7016 | -46.902199 | 2025-09-08 00:25:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 478c25ed-4eb4-3e1c-8391-373a9412f280 | -11.5881 | -47.160198 | 2025-09-08 00:25:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f60121e-8036-3d0d-84b5-4a9fb3f24e9a | -6.1206 | -44.241501 | 2025-09-08 00:25:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a51c581d-89b7-34b0-8f71-db7071ffccdc | -5.9285 | -46.165699 | 2025-09-08 00:25:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c283d7d8-8bdd-389c-9986-fdf6a5a9c995 | -5.8653 | -43.982399 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9fd2058e-5113-3b8c-ac59-e2c48332489e | -6.1866 | -41.010601 | 2025-09-08 00:25:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab0c801e-0d12-30e7-b1df-e978970477df | -9.679 | -43.5243 | 2025-09-08 00:25:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1bd20f7-cef8-33f7-97ce-e2aeb948db64 | -5.444 | -42.826099 | 2025-09-08 00:25:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 30849f24-ad29-33d8-9345-791a948cebcc | -19.4835 | -47.869499 | 2025-09-08 00:25:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 32167330-cd3e-3ede-ad84-fb573f38d05b | -6.9595 | -45.577599 | 2025-09-08 00:25:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55632792-7f7a-3256-a0b0-a0159a3ad243 | -8.2088 | -44.7687 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b3bd5fd9-bdd4-3ab3-baf1-d20f161b4d4b | -11.3967 | -43.6017 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09238e68-c08d-3f69-8946-c3bbd7b3b41c | -7.0968 | -44.1371 | 2025-09-08 00:25:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6d1af824-0158-3b25-9e63-b9c5221956b0 | -11.2629 | -46.453201 | 2025-09-08 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11eb49b2-6197-3861-9262-17d52ed02fe0 | -13.6815 | -45.492599 | 2025-09-08 00:25:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7eac76d2-e799-3f04-b64c-9d0d492ba3a4 | -5.6295 | -45.1171 | 2025-09-08 00:25:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d06aa1e1-019e-3a46-9d8f-ca12f474a3c4 | -6.8226 | -44.880001 | 2025-09-08 00:25:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 964e9d26-9f61-3d5f-b942-320ac2f0e6e0 | -6.104 | -44.259499 | 2025-09-08 00:25:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9411df6-ef20-363d-bd6f-9bba3808eba9 | -10.7999 | -47.7365 | 2025-09-08 00:25:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 668a4b0d-6212-3f71-88e7-1b37bc242cb9 | -13.3393 | -44.429001 | 2025-09-08 00:25:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1cf0ecd-3f7a-39b8-b4cb-99d539caecf7 | -7.9743 | -45.4669 | 2025-09-08 00:25:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f9e6ab20-015e-3d65-a7ac-426c7890ed3d | -6.8681 | -45.537399 | 2025-09-08 00:25:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87bf8498-33f7-3a60-9972-da27a3d09aa4 | -19.9541 | -44.3022 | 2025-09-08 00:25:00 | METOP-C | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39aaabc1-00ca-3811-8bac-2ed9465144a4 | -14.4911 | -48.787399 | 2025-09-08 00:25:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3dbaffb3-d005-3c6f-99ad-318e9afbd6de | -11.1177 | -46.350201 | 2025-09-08 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 797ebdc3-f70e-3ae5-b908-8a1052b815be | -6.2026 | -43.3853 | 2025-09-08 00:25:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 534ff6dd-a157-3f99-8512-2dbc58a2208c | -11.3743 | -43.547901 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d6bfc999-8c2b-333c-a96e-5bc072de63b4 | -8.6819 | -45.3176 | 2025-09-08 00:25:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4bd3773b-289b-3c2d-bb4f-f53c451e2c50 | -9.9775 | -51.668301 | 2025-09-08 00:25:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03e4bb38-4a05-398b-8629-61804556f308 | -17.1357 | -44.429199 | 2025-09-08 00:25:00 | METOP-C | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fd18f719-dcbe-398c-9a67-86ea6efde519 | -6.5112 | -42.933601 | 2025-09-08 00:25:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f873218-590b-3a7e-b93c-666bf5e7903c | -7.0715 | -43.8904 | 2025-09-08 00:25:00 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c35b5c65-910b-3098-8cc8-9abb67b47a1c | -8.7261 | -46.6772 | 2025-09-08 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 755a1b1e-fd46-3956-af75-be67d1fc5e94 | -11.1129 | -48.397701 | 2025-09-08 00:25:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8be34b-5cb8-32fa-90a0-3d7f4c6cb46b | -7.404 | -49.2631 | 2025-09-08 00:25:00 | METOP-C | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 65e4c079-7d34-3a8d-997e-a2fe1098ae77 | -6.5957 | -44.019402 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f27f95a-a153-3347-a3e3-9befa74c2c95 | -19.1703 | -42.076199 | 2025-09-08 00:25:00 | METOP-C | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 786737a4-e8aa-3177-9d89-cb1437dfb231 | -6.5941 | -44.0126 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b7af31b-1129-3bc7-8977-05b1229bb43c | -9.1848 | -46.054501 | 2025-09-08 00:25:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e60a2380-6417-3531-b4aa-403c30d14e1a | -16.528299 | -45.101002 | 2025-09-08 00:25:00 | METOP-C | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 162a01d2-b10a-38b8-8542-04704b51f564 | -6.5749 | -43.973701 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38e5732c-7a22-3510-9fe2-9483544cbae3 | -11.1106 | -48.3866 | 2025-09-08 00:25:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4bcb7fdd-695f-3359-8771-d76f8498cbde | -7.9569 | -44.839802 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c78e65a-5f17-3ed1-be8f-c9a1661082e8 | -4.6435 | -46.357201 | 2025-09-08 00:25:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8aad77da-3662-3512-ae72-e88605736d73 | -6.8421 | -45.925201 | 2025-09-08 00:25:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21e5a09c-81d1-312a-9229-cee4648976f6 | -6.5545 | -51.098202 | 2025-09-08 00:25:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99798a6a-a58f-38a1-a3fc-da00f36f85a8 | -16.271099 | -45.6875 | 2025-09-08 00:25:00 | METOP-C | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c5d827ba-5ca6-3e56-89cc-9cae82f4add2 | -12.5227 | -49.1068 | 2025-09-08 00:25:00 | METOP-C | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef0f7047-950d-3056-bcb9-32f13b41c039 | -8.6803 | -45.310299 | 2025-09-08 00:25:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 90282844-ea2a-3200-859c-dd6136a93e7c | -11.1354 | -45.251999 | 2025-09-08 00:25:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be4cb621-d6ee-353e-8139-b1c9d8158257 | -6.2443 | -42.583302 | 2025-09-08 00:25:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5226a3b2-ced9-3eba-a103-c2b5e8b98267 | -8.1923 | -44.787201 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 955b1f78-8c18-379a-8ce2-32f221f8501c | -11.1812 | -55.023998 | 2025-09-08 00:25:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 56764fa4-d741-3a26-9b67-d5db659e1261 | -18.0119 | -47.108002 | 2025-09-08 00:25:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 23fc9801-c0da-37d6-9f14-00cbdc77efcb | -5.8567 | -45.073799 | 2025-09-08 00:25:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85b798a4-d1f5-3319-85cf-56d6b3d13aaa | -7.9746 | -46.344601 | 2025-09-08 00:25:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ea12af9-6306-3c79-a67e-a7bc7507298b | -15.169 | -47.952499 | 2025-09-08 00:25:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6cb3633d-ee3d-34cf-9490-99f505048674 | -5.2035 | -43.7057 | 2025-09-08 00:25:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e5daf67-fccb-3742-a5fb-51e4961891cd | -11.3904 | -43.5737 | 2025-09-08 00:25:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a69eb47-4585-3a7e-8b11-ef12f9778867 | -13.0135 | -47.130901 | 2025-09-08 00:25:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93f4c3e6-3b86-3ca8-a27b-4f60ba545a0f | -16.8981 | -45.806301 | 2025-09-08 00:25:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b02f437f-96f4-3e33-99c7-1de0be4fb818 | -7.0984 | -44.143902 | 2025-09-08 00:25:00 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 47319ac8-d8e5-34c0-8508-8a37241580d9 | -13.0254 | -47.138802 | 2025-09-08 00:25:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab720993-aa9a-3ec4-b7c1-fc41e8949b37 | -5.4189 | -42.6731 | 2025-09-08 00:25:00 | METOP-C | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 765c4e80-465f-3cf0-95e9-db7ad516c635 | -5.8468 | -43.856899 | 2025-09-08 00:25:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f22755f2-a5b0-3b64-9900-3a832481fcac | -8.1958 | -44.756901 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6b590f11-ff92-3704-84be-d7325716b3d0 | -10.7782 | -47.730701 | 2025-09-08 00:25:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5bd4330-e16a-3eea-baad-870bfaa5e61a | -7.0794 | -42.937 | 2025-09-08 00:25:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6530c062-b194-3146-b132-ddd07e6757e2 | -6.5784 | -44.1241 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f639d63-dfed-31e1-b93d-d6196a5bbd8d | -18.3426 | -43.929199 | 2025-09-08 00:25:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| be8ce24a-5be6-3081-9e48-8e546ec303d9 | -16.5301 | -45.1096 | 2025-09-08 00:25:00 | METOP-C | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fa77c11f-f2fb-316b-8293-55538a990a24 | -6.4467 | -43.191101 | 2025-09-08 00:25:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0d214b3-d104-364b-92fd-a2be5036b76d | -17.5996 | -44.839199 | 2025-09-08 00:25:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 76ffcd57-bb67-3a4f-b410-403e96ff2347 | -8.0633 | -44.808601 | 2025-09-08 00:25:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f5d97e84-3629-35b7-a27c-7f9fd0a5ee26 | -6.4701 | -44.0117 | 2025-09-08 00:25:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccd83d42-5d9f-3fa2-81a0-9b589fa74259 | -11.1848 | -54.9907 | 2025-09-08 00:25:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 927bd5c6-4525-38ad-b6d9-07ad99c7c7b7 | -9.8466 | -46.590698 | 2025-09-08 00:25:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86dfaeea-6db1-3547-a1c0-58f8d2c45797 | -7.0718 | -45.2076 | 2025-09-08 00:25:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81bd961e-c75e-34f0-ac9c-b46c94f41783 | -6.2414 | -43.6884 | 2025-09-08 00:25:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
