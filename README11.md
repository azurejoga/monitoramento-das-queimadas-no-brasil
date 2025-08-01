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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f697617a-b1ca-3ae9-be19-3413d8242d0f | -15.9512 | -47.7531 | 2025-08-01 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 129c5c4f-1831-3f4c-b7e1-3460effd3efc | -14.33352 | -48.65633 | 2025-08-01 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2b6bb4b-a10c-3919-a374-ab6c115eadbc | -13.22465 | -47.23677 | 2025-08-01 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9004c7b4-07cb-37f2-9ec1-c7611feae5dd | -12.09697 | -44.98289 | 2025-08-01 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a54aa24-e7fa-3d7f-a5fb-fd8b16696eec | -13.37146 | -43.75672 | 2025-08-01 03:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3053ef62-bc34-3da7-8854-0087a2351022 | -10.43437 | -47.26745 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23875b21-3ecc-3b1d-bd68-1c9e70597d5e | -9.9742 | -47.69659 | 2025-08-01 03:51:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6699a824-406a-311a-9bcd-ff3947670c24 | -12.26924 | -45.06846 | 2025-08-01 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0744e096-d102-3c8a-8383-7c6418a0638f | -8.24594 | -49.57265 | 2025-08-01 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a73abfe6-906e-32ed-b8aa-4c1e5c3e1db4 | -10.60032 | -46.21644 | 2025-08-01 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d367ae22-096f-331d-8372-04a486921c81 | -8.24397 | -49.57226 | 2025-08-01 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75edd01b-7097-3c11-a413-10f0daba8781 | -11.77759 | -45.00575 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3883871-7cd4-346c-81e7-00f7c4903c11 | -14.20552 | -42.84304 | 2025-08-01 03:51:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5ed9b43a-e600-306e-b728-e597e1a5ad57 | -10.43644 | -47.25665 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0837cde0-f1d4-39e8-9871-6a1ff6b548f2 | -12.42801 | -44.71844 | 2025-08-01 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9fbcfdd-fa7a-3a2c-8eee-abcfb861955c | -11.78119 | -45.01212 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78b991c4-08de-3194-aaff-d9c2d1042588 | -11.76842 | -45.00393 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9276e89-0f4a-3bea-89b8-4c1367e9fefe | -11.77664 | -45.01101 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae83fec2-c7ae-3851-9599-b9b51b8ae981 | -10.43713 | -47.25308 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9de72b86-72a0-3b29-9c6c-88e5fd59e54b | -12.44081 | -44.74907 | 2025-08-01 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf92d337-570d-3d08-bee8-3addf3bf829c | -9.80492 | -47.06118 | 2025-08-01 03:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75f2e7ce-6d20-3163-89a9-a1c8b761a5fe | -9.7456 | -48.66734 | 2025-08-01 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfbc8bb9-9168-3f85-a7a5-53200ae84c11 | -11.77051 | -47.39559 | 2025-08-01 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e4a6166-bb8d-31af-809c-4fd06827731f | -10.42959 | -47.26284 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b077af9-5f4b-3d50-8585-5a2247e72082 | -10.60383 | -45.27532 | 2025-08-01 03:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8d1a939-6ec1-3723-9965-b8c0bfc3a426 | -8.25051 | -49.57353 | 2025-08-01 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29a26900-0bfb-3ff6-9300-2e2e84082eb5 | -12.10152 | -44.98382 | 2025-08-01 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8daf6cdf-6e1c-33a1-8dac-5e04161a20d4 | -12.75359 | -44.4194 | 2025-08-01 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50594ad9-a1e9-3a7e-9df2-19c7cd0913af | -9.47074 | -47.80296 | 2025-08-01 03:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0dd6c2bf-cb28-3233-bbf4-e043da9a90af | -8.33729 | -50.57896 | 2025-08-01 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d0f68389-73c7-3dbc-ad43-4d57757b81ca | -8.25248 | -49.57394 | 2025-08-01 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f804996d-8f5d-3ae8-abff-addda2ba7f5d | -9.4715 | -47.79902 | 2025-08-01 03:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cad53c61-3817-3f59-a346-ca81409ac9b5 | -9.79983 | -47.05761 | 2025-08-01 03:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed9c7341-f8b9-3deb-8cff-060ca26cada6 | -10.42959 | -47.26411 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 705643de-8214-3f4a-985e-d5851a5969ff | -9.01345 | -47.97676 | 2025-08-01 03:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfb7e38e-95b3-331c-a01d-27ab4c9bd191 | -10.08609 | -46.74708 | 2025-08-01 03:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20ef360a-3dac-38b6-8959-3cdfef8c9357 | -10.44119 | -47.26143 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c6c83f7-f49d-3675-b4a0-51dca50ebe92 | -10.08356 | -46.74519 | 2025-08-01 03:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1143186-e7fd-3293-bdba-c6fdc31596ea | -10.4289 | -47.26641 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2b512b6-d1fc-3f97-a1d9-8c80aaaf12d8 | -10.08296 | -46.74846 | 2025-08-01 03:51:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efed646a-4e48-34fe-b6f7-44b9e9c23dcb | -11.77522 | -47.4002 | 2025-08-01 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5cbff65-2332-3cf3-b48b-5bdea19a7229 | -14.37813 | -50.32926 | 2025-08-01 03:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 255a0116-a324-3aa9-843b-a2ca891543c8 | -11.52138 | -44.3241 | 2025-08-01 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e1de386-3c43-3fb1-8592-1e6891ba99af | -10.42893 | -47.26767 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17c61af1-c58b-370a-b921-d580234cbdc5 | -11.76183 | -44.988 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 998e9b05-f783-384b-a6da-911a66411126 | -12.05231 | -45.439 | 2025-08-01 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a94eaac-e974-31e6-b11f-621fd826678a | -9.01928 | -47.97802 | 2025-08-01 03:51:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04c4b049-c772-3381-9eea-4f39b35b4a4c | -10.43575 | -47.26027 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 626b208f-c1d4-3064-af17-173938b64012 | -11.76094 | -44.99289 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40888b53-9eae-325d-9e80-0b295dd9a9b3 | -14.32789 | -48.65552 | 2025-08-01 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 595c4334-fbb7-3e97-837b-bd389c974ca6 | -12.55706 | -44.73171 | 2025-08-01 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a192241-af2f-305a-acbd-780a51903053 | -10.43165 | -47.25212 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11ea7b22-2d9d-3c61-a52c-c7f5936b25ad | -11.76646 | -44.98862 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 641ee5c6-b182-3255-bf0f-021e20b71226 | -12.26456 | -45.06815 | 2025-08-01 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5aa3d03-4f22-3703-90fa-ae38f7064113 | -9.85258 | -44.70694 | 2025-08-01 03:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dc8319f-1217-3725-a5a1-605b5a3d6714 | -11.52658 | -44.32057 | 2025-08-01 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66cdf92d-64bd-36b5-a19b-b072134ef38b | -15.66557 | -39.17236 | 2025-08-01 03:51:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ec80d0f4-dfa3-3d22-884b-ff376e901ba8 | -9.58826 | -43.84372 | 2025-08-01 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 00c29d9f-b460-33d7-aa79-911add6f5b22 | -16.13601 | -46.88309 | 2025-08-01 03:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c7b439f-972c-37ba-84fb-90361eefe63a | -9.80423 | -47.06481 | 2025-08-01 03:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bdb9264-075f-3990-a7c1-2c2d51418cbb | -11.75811 | -44.98242 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51993c68-77c4-3f62-8419-940ceb60e603 | -12.26545 | -45.06335 | 2025-08-01 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2ecb0d0-2654-3529-a196-ba6b746dafaf | -16.13706 | -46.87779 | 2025-08-01 03:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 308bc412-9225-3aff-be28-d72d70d8809c | -16.13227 | -46.87679 | 2025-08-01 03:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d50964c-dad3-3b02-9aee-064b459a07de | -10.46018 | -47.28064 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5211e3d-1dfe-3df2-ab7d-0d5cbeffa165 | -12.55261 | -44.73087 | 2025-08-01 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05ea2432-28af-3db1-91fa-ddd3ee32c247 | -12.26836 | -45.0732 | 2025-08-01 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2df3b19a-05e9-371b-8ef9-b91f4da048cd | -9.85724 | -44.70775 | 2025-08-01 03:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f6187ad-ad7f-366b-a2ef-44e2985f40c9 | -9.73953 | -48.66634 | 2025-08-01 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f755e777-54fd-364c-8a42-9d68f1bbf678 | -11.77588 | -47.39671 | 2025-08-01 03:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7811f5d-7b4f-38eb-96d0-e5b170761c03 | -12.43244 | -44.71935 | 2025-08-01 03:51:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b32b033-6f46-3995-8fba-3bd6a30eb1c6 | -10.46088 | -47.27698 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f82d4988-9629-3f6e-80ea-ff32fb2541b9 | -15.88997 | -48.18695 | 2025-08-01 03:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0009358b-bf75-3cd0-819b-4cd1e782ef6c | -8.32912 | -50.58405 | 2025-08-01 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18e52c46-8c45-3d0d-be13-ce2e2f8528e4 | -11.77392 | -44.99982 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b098a44-b946-3800-a0d3-b32f5a0f3e5d | -10.79642 | -44.24481 | 2025-08-01 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34514d1c-6efd-3846-b652-00d21554b06e | -11.77205 | -45.01009 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 640577d0-aa55-3cda-abc2-4d4c107287e0 | -11.76745 | -45.00927 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b178ea8b-adbc-3122-846c-a1cb8e3887a2 | -9.80016 | -47.05656 | 2025-08-01 03:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fe8dac7-138b-3043-aad7-0fc9d008fd49 | -11.77302 | -45.00475 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9c92e7f-1557-3784-aef9-2ffe143377c5 | -10.32146 | -39.21383 | 2025-08-01 03:51:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f6a07d5a-c850-3d3b-b2e3-c1c9174dcc7e | -8.33038 | -50.57757 | 2025-08-01 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65e72363-c7d6-3616-bda8-5793f1abcca0 | -10.60471 | -45.27051 | 2025-08-01 03:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bcd0e52-c89f-30ef-9f49-61fb29c9c198 | -10.59977 | -46.21946 | 2025-08-01 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81678409-014e-3584-9e91-5be6305156f9 | -16.1264 | -46.88115 | 2025-08-01 03:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3e8a4eec-fdeb-3c0a-b188-7da25a785af6 | -10.79819 | -47.26244 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90ba149c-195f-3cfe-a7fa-cd45d223ec99 | -11.76932 | -44.99897 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fce6d99b-429f-3b58-8bfa-163d53ec7971 | -11.76558 | -44.99345 | 2025-08-01 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a78984e-daee-3519-b549-0ae977d6189e | -10.45612 | -47.2722 | 2025-08-01 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffef966f-965a-35ae-b8e3-8fc32b703579 | -9.47077 | -47.80301 | 2025-08-01 03:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6a532b0-7097-3dc4-af36-d3d5261f8d29 | -16.12748 | -46.87574 | 2025-08-01 03:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d217d70-0a52-35bd-9346-ff464f7c876c | -9.80462 | -47.06225 | 2025-08-01 03:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 219d4925-0726-35a6-8ecc-d7ea9e0ab87b | -15.691 | -43.20942 | 2025-08-01 03:51:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2eec6c7d-1cde-3fe9-92ce-49fcbbea78d5 | -13.22386 | -47.24077 | 2025-08-01 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| be4e2cbd-1e17-39bd-b49e-e620f096301e | -12.81122 | -45.43803 | 2025-08-01 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d1a7dd5-462d-36c3-9333-e3cd7b7efa61 | -22.59376 | -42.10807 | 2025-08-01 03:53:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d298ae80-5918-37df-b7a5-2030a9f46d54 | -19.79963 | -44.655 | 2025-08-01 03:53:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 81bb49e3-a54a-39cd-a0bd-a22cb3cb5a8d | -20.43921 | -46.4267 | 2025-08-01 03:53:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59b3a89a-9744-36f8-a056-2079402ead01 | -20.44001 | -46.42957 | 2025-08-01 03:53:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9678373-cb89-3db1-9861-d7cd7a7ff702 | -20.34833 | -45.99091 | 2025-08-01 03:53:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README12.md)
