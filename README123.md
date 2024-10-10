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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb61d809-b9e1-3468-a6fc-ce7ed66ed6d6 | -11.95893 | -57.60076 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86b15d83-8535-363e-b0dc-f1a84480a942 | -11.27741 | -57.87674 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3164817-92e6-366a-8800-c9446ea822c4 | -11.04344 | -57.21469 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f955d91-77cc-3256-9dca-1e8af375104f | -11.04159 | -57.22549 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 22a5f547-3e65-3164-a0a6-337c4171f089 | -11.04098 | -57.22907 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a2c1c6a-8072-3235-bdab-745c6d0db154 | -11.04001 | -57.21042 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a271f6e6-d464-3e6c-b798-4733df18cd92 | -11.0394 | -57.21399 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b888b5d-b6ca-33ce-913c-cbb3cea1021d | -11.03878 | -57.2176 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc4da2e3-3ba3-3cda-802c-aeda86de7b0c | -11.03816 | -57.22121 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49982632-a540-35e5-b65a-43ea9d2ac394 | -11.03755 | -57.22477 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c0979fe-456e-3ba1-909d-8d742922dc93 | -11.03694 | -57.22833 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 501d0056-84c5-38b0-b9ef-7a9b7b93567c | -11.03597 | -57.20972 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e10e27fe-1fdd-30b9-a559-b87d915ff3cd | -11.03536 | -57.21328 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 818c2bec-4a0c-3817-8360-a0ce4118c5cd | -11.03474 | -57.2169 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bd301cd1-c17b-3aa2-9617-5533ac2e8b0c | -11.03412 | -57.22051 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ef480d1b-28db-3bee-8f10-e347f57cbc57 | -11.03351 | -57.22408 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b1a2ed20-1343-3ed3-aa18-07faeca2efc7 | -11.03289 | -57.22765 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7051904-905e-3b28-83e4-647dc5b3ebad | -11.03227 | -57.23128 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bce6a31e-17dc-37ec-a605-2b8b19a244a1 | -11.03193 | -57.20904 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 900be1c8-06a7-3d27-a981-9a3562b7ecd7 | -11.03132 | -57.21258 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c6053866-8616-3bd4-a82b-2c7c8ef1ca20 | -11.03101 | -57.23862 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a98539e-c12c-343b-927b-20244fb95945 | -11.0307 | -57.21618 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3ad486c1-9134-3b1c-b38b-1583062d2776 | -11.03039 | -57.24223 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 40ce1ce9-d614-3698-b417-6741928cdedc | -11.03008 | -57.2198 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dfc968ec-096e-3445-9286-5666d4e21bae | -11.02946 | -57.22338 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3fb577e4-6e03-3b79-940f-ab338d7b9eb1 | -11.02885 | -57.22697 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 942a2bff-9b3e-3dab-a713-aa9e0137a551 | -11.02823 | -57.23058 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4da4d566-efb0-3bfe-ab10-ef6796605ce9 | -11.02789 | -57.20834 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c8bb5a95-de2a-353b-af82-5b49027daa73 | -11.02759 | -57.23426 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1df0b2ef-621d-3c16-8357-ebc61a2bf9ca | -11.02728 | -57.21188 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9596b66-ed03-3fac-84a7-667380a4a720 | -11.02696 | -57.23793 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f54aad39-515f-32b4-9042-2fcc00f09aa9 | -11.02666 | -57.21548 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7803dcb1-938f-3774-bff9-f4a397447c86 | -11.02604 | -57.21909 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90b6f737-4b56-31d1-8c95-b012bb3e0914 | -11.02542 | -57.22269 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 404ada3f-b611-3e2d-a399-735a2ec72fbd | -11.0248 | -57.22626 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e329a2f3-55ef-3b8f-9b08-1e631e87581e | -11.02418 | -57.22986 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a53fe5b-9744-3f66-99f0-5cff937beaa3 | -11.02355 | -57.23355 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad1295bc-8af6-3dbe-b508-d743338e35f6 | -11.02292 | -57.23723 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6882c53d-033c-362b-998d-0f4c9a826c03 | -11.02262 | -57.21477 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 503660bc-7610-335e-8c58-6f513b6e0a6a | -11.02199 | -57.21839 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15af6f65-1e6f-3857-8e8c-edfbdf901072 | -11.02137 | -57.222 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a1e44db-af60-379a-8d9e-ead32fef1624 | -11.02014 | -57.22916 | 2024-10-10 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a128a3ac-0d4b-3e59-92f6-8e2cbeb0fc3a | -10.69983 | -58.54227 | 2024-10-10 04:46:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 181a0176-1d7f-3743-a536-8a537f24dbc4 | -10.69904 | -58.5466 | 2024-10-10 04:46:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 307d0e27-3fe5-3305-b8b9-af227236a4c9 | -10.69623 | -58.54305 | 2024-10-10 04:46:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f232f23-f856-31e0-90a0-e5b2f62abe42 | -10.68737 | -58.54141 | 2024-10-10 04:46:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42e26268-0767-3600-8138-99fa4eac669a | -10.57689 | -59.50062 | 2024-10-10 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c919edeb-2f68-3234-be9c-8cde7ae955d2 | -10.57216 | -59.49972 | 2024-10-10 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0daf04a2-30ba-344f-87f1-5143b9f99152 | -10.57121 | -59.50491 | 2024-10-10 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbc4bc2d-781c-38f5-846b-83f95d446225 | -12.32534 | -59.19971 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51fd1a70-f796-368b-98ab-46da893877d6 | -12.32282 | -59.19732 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 609a41ff-42f4-3669-9ced-5eb18b10db89 | -12.31686 | -59.16919 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da3ff190-0b55-36c6-92ac-9d5f72bb9823 | -12.30703 | -59.17224 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a962a36-34b0-3cfa-beea-0ed6e9f90fd6 | -12.30252 | -59.17145 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c667505-abde-321d-95aa-94a89af2f76d | -12.30169 | -59.17605 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fadf1ba8-8cb6-3046-95fd-234557f08f46 | -11.89255 | -59.45362 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 776f8c37-30dd-3236-b66c-4955d811d458 | -11.89166 | -59.45847 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14e4db80-3eba-309f-b87d-533fa70ac288 | -11.81829 | -58.84549 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91bc3164-be8d-3142-a49c-41dc10ec917a | -11.81749 | -58.84997 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f87d0f37-c16b-30b7-9776-abc6b26f48fa | -11.81465 | -58.84024 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fc00b48-3762-3083-a57f-c46e0590de6f | -11.81385 | -58.8447 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac4a4b5f-c0f3-3427-a00b-694c3d87146a | -11.81305 | -58.84918 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e49748a2-28eb-3517-bbd1-86f6df7eec19 | -11.80941 | -58.84391 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1829c441-7df2-314e-bc41-62c4795c1571 | -11.80861 | -58.84835 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 845fece6-4167-3a2a-91d2-479bdf412a25 | -11.80814 | -58.8255 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d09110cf-c575-36e5-a86f-d26a3c3bc05d | -11.71858 | -59.29535 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ea2b24b-103d-3f3b-929b-a3defafd3970 | -11.71119 | -59.28392 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bca59ad-bd68-3b39-baaf-055b58b34553 | -11.71032 | -59.28873 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d34745d0-a5fd-35f9-9128-f2f150294e17 | -11.70896 | -59.14187 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7813c2b5-77f8-3acd-9050-060fb2440372 | -11.70575 | -59.28783 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 364d2d90-2617-3f50-9332-b92818d0298c | -11.66876 | -58.89368 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 541531d4-f426-337b-ab7d-f56950f8ca99 | -11.66794 | -58.89819 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 374f53d0-7445-3c93-bc16-d4e8565ecc1e | -11.66429 | -58.89289 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 98a34d34-e608-3ecf-bdd7-d051cbd91296 | -11.66347 | -58.89738 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d98732e4-e09f-3830-872e-ba21503d2f50 | -11.37805 | -59.19429 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c6cf02f-8c41-3419-9734-8b743d3e4ace | -11.13181 | -59.09544 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1c0e973-ed8c-3730-a328-f38fd811820e | -11.12729 | -59.09439 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b934dd9-b4d3-3683-9feb-851f158002b5 | -11.12641 | -59.0993 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11ae68e4-7fb2-31fa-9621-fe64cce0b5d7 | -11.12271 | -59.09364 | 2024-10-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3cd54d0b-7d0a-306d-bd74-057877299888 | -10.43074 | -60.99423 | 2024-10-10 04:46:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ede6ad98-ff68-352d-899e-7433f5d813fa | -10.43016 | -60.99737 | 2024-10-10 04:46:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a6bd4a2-d136-3946-a061-66c6907ed8fd | -11.40153 | -60.40324 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a883fd92-4ab7-3eae-b2b8-1620570a02b8 | -11.3955 | -60.40806 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13cfd3b3-8409-3865-b197-dd39d4100449 | -11.3933 | -60.41989 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96067be0-dcbc-33b1-9d27-520c8080ac95 | -11.27123 | -60.49382 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cb9001a-30c6-3d26-a30d-7a3efb460477 | -11.26789 | -60.40123 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 07eb8152-ec5f-3c1b-ada6-276053d504b4 | -11.26677 | -60.48999 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b4a0f1d-91fa-3423-8f07-06d6cd543615 | -11.26673 | -60.40745 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e8868f7-8576-3a79-83c8-005b5b4fb103 | -11.26624 | -60.49283 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42071a7b-3f0e-3bc3-91be-ca6b19260d62 | -11.26571 | -60.4957 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc6f8daa-c638-3666-8622-56b5f0cd4311 | -11.26516 | -60.49862 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b975b7ce-a14a-36db-9399-cc69aa93fa07 | -11.26169 | -60.40688 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6dce31d-1809-3339-9643-2cf028957c56 | -11.2602 | -60.49747 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91189ff9-2f53-3509-89ec-b43c84054b24 | -11.25965 | -60.50039 | 2024-10-10 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b13a5a9a-ca87-3122-bbcd-439d7f0d3b29 | -11.16143 | -60.61325 | 2024-10-10 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea7997f8-a06d-342e-8df9-8cc1596b3608 | -11.15637 | -60.61234 | 2024-10-10 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| debdeda8-b68a-3c94-b674-7cbef110ce9f | -10.3632 | -55.8554 | 2024-10-10 04:46:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| da9081dc-2c1e-3c65-b3d8-0fbc1117ba6b | -10.6832 | -51.0907 | 2024-10-10 04:46:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| dfb3c81f-65c3-3912-9d4a-a725f2ac4332 | -11.0445 | -57.2023 | 2024-10-10 04:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| df33147e-27af-38bc-8b01-729f00fd142d | -11.0254 | -57.2237 | 2024-10-10 04:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |


[Clique aqui para ver as próximas entradas](README124.md)
