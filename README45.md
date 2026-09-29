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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f5f2ee0-ab53-31b6-a90b-f5db5eb25673 | -11.19598 | -44.79923 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcdb31cf-94c2-3430-baaa-189adc78398a | -9.81918 | -44.94171 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7d922a5-630a-3683-a3cf-fe6c028c29d0 | -9.96634 | -50.12703 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14f644f1-5843-337d-89c2-f151cac4c7e5 | -11.86063 | -47.08129 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 56e0a1c7-1565-3bb2-8df5-11d7126f1bf1 | -6.31824 | -52.61923 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8086c97f-0015-3b0b-9068-36a72a8ce9d4 | -9.8271 | -48.20745 | 2026-09-29 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40a4cedc-1564-3d80-b4f6-54881fa22b0e | -13.22318 | -48.5552 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65ee1d56-5298-322c-9f80-36e298de5853 | -13.2674 | -43.5497 | 2026-09-29 04:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb91456b-16fe-301e-95ed-07a8cee54a2a | -7.88969 | -54.72555 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25f17ad6-d970-3302-900c-95f00aeba45f | -6.14342 | -51.73867 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ed48f6b-211a-30d5-824c-be8c9acb6a92 | -8.64127 | -45.34867 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd90d544-6952-3a24-bd61-d883eaf48735 | -13.73794 | -43.66855 | 2026-09-29 04:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5dba3546-8d7b-3ffc-989f-1d1302468500 | -13.16778 | -48.56614 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70bb9b91-9e55-3b21-8d2a-8e0ef8d5fbc2 | -10.28297 | -44.63614 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9cc8e0b7-00f9-3f4e-8708-48570c57e7a2 | -12.91026 | -52.07486 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abd39239-1568-3fcb-9862-a6a26eaeca6c | -7.25962 | -45.34114 | 2026-09-29 04:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 656262d0-b9cc-3324-98a3-a3eb847077e0 | -9.14459 | -49.97401 | 2026-09-29 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94ff9912-9bfd-3fe1-ae86-bf0607245c87 | -12.00555 | -50.93809 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 80d20f9c-987f-3cef-9ac2-b28ae9f3ec10 | -6.13902 | -53.06168 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32e11b8c-d5a5-3d05-963e-a00710031a69 | -10.80783 | -48.71932 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba1b9673-e9be-3562-b19f-64560df164f1 | -11.95722 | -50.94101 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 888f93ed-40dc-3f97-84cc-44fb1e469d56 | -9.76363 | -36.97924 | 2026-09-29 04:51:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 86da936b-84df-33b3-8ac6-4aadee79ab11 | -8.22845 | -45.4754 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76397e4e-3e7e-3bd9-9aa7-8dbfb93baf29 | -11.38425 | -43.39139 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89a37a44-e67a-30b3-88d3-ed77eff003f2 | -6.14774 | -52.91085 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68d9efef-d0bb-348c-824b-654e3fb9b3c3 | -13.11284 | -47.41343 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d9fd7d7-e079-3cae-95f3-6530e6e7fea9 | -9.16714 | -61.4125 | 2026-09-29 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcbfcbea-678f-3aa0-855e-e60ea92df311 | -9.78452 | -44.81686 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 853aa1f5-02b6-3e45-abc1-ea943879c40a | -9.7863 | -48.22034 | 2026-09-29 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 203fcffe-2dd4-36fb-8978-03ee4bddef3a | -11.93339 | -50.91895 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2476858-bee8-3aa4-888c-e32eb817631e | -11.34855 | -54.04162 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bab6d5a3-6326-3dbd-91ae-04bb2ea9fffd | -13.08843 | -47.43917 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd9700ab-0e9d-358b-a9d1-2336d31a4658 | -12.77408 | -52.81593 | 2026-09-29 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14975ab5-c2c1-3e2f-af32-5098ef804b54 | -11.42747 | -43.44391 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2d650da-cde4-3899-8407-b194a3db9647 | -8.67809 | -45.34409 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08f4025c-e366-358b-af69-010c212191b4 | -11.93785 | -50.91243 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36b82edc-824d-3363-a5b8-95c25b96463e | -10.81524 | -48.71666 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7404ca30-9576-3076-97c1-f7cea7f8f80f | -11.34842 | -54.10959 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b4d798c-f540-39da-ae7e-8f50c020a7af | -7.51782 | -46.61185 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08cbe990-0c09-3ed5-91aa-a73f778b3cdc | -11.71704 | -43.45992 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e686a460-f5f0-3570-9695-5dbe337a7c27 | -7.95625 | -49.5763 | 2026-09-29 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a892e11-af32-3aab-b468-8cdfd2ed617c | -11.38317 | -54.03859 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32668f9d-1baa-3432-9e63-f98f62a98f4f | -11.13062 | -48.3339 | 2026-09-29 04:51:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1f63d12d-edca-360a-8f53-7baae8f1898d | -10.79308 | -48.74711 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b14ec0b-542e-3eaf-a068-bb6d41d51953 | -13.52198 | -46.91558 | 2026-09-29 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21e3931c-8cae-33f4-8f75-ae1cec1802c7 | -12.73909 | -47.27958 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cc18a547-7059-39d1-a6b1-0fb5b04a1894 | -11.17651 | -44.78564 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c89ddb5a-5c76-3184-a05b-9e023b4662f0 | -11.35886 | -54.04794 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5db8c1bb-c4f5-3e3c-b548-65b4e36dcafd | -11.17595 | -44.7896 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| cbd76499-7138-3690-b91e-a52e57b7bcb1 | -14.08481 | -46.31021 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0481657e-89ca-31d2-a9e7-15657e10721b | -11.99218 | -50.95759 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 157f3b4c-45a9-37a8-ad32-db7d89cb242b | -6.67852 | -55.11317 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1aed522c-bb3e-30dc-8508-ddb3caf8b024 | -8.24353 | -45.45367 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5971f247-2523-3045-94b4-a7cb17601442 | -11.37727 | -54.05116 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2c057bc-02a8-33f5-9032-622ab472be4a | -11.95445 | -50.93693 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae486356-1705-3510-a2c3-505b37272011 | -11.35736 | -54.05678 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7c28ed6-d486-326a-8202-d3d237c2b67f | -8.22652 | -45.40681 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30de125c-1466-3fc9-ba4f-a9899b95489f | -9.95523 | -50.15401 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6aad08e0-e3c3-3e20-873e-763c8e88e238 | -12.43938 | -48.216 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 413b4ec8-967d-3792-aea2-218f32dabb1f | -13.17536 | -48.56334 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d9b3fa9-031a-3325-b913-7275293f29e8 | -13.09117 | -47.43311 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59226724-3fa6-3dda-a53f-6da761a61f11 | -10.81867 | -48.71711 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97449855-1ddf-3ada-b4b5-628e2e780cf2 | -8.24497 | -45.44389 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1096fcf8-ad77-341c-bcc1-60f4cbf267bd | -11.36179 | -54.05303 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72179fb1-f850-3dcd-a2bf-6e8846b6f67f | -9.40329 | -46.83851 | 2026-09-29 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c1a319b-8fa0-371d-820d-b5283549877c | -6.14846 | -52.90645 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11d66f63-d887-3376-b456-39ddded46f30 | -13.08996 | -47.44164 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6dbc1ca1-92c8-35ed-968d-cb51f3aed7b9 | -12.77395 | -54.02784 | 2026-09-29 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6882a76a-ea6c-375f-bf17-f6deecb38f05 | -13.09058 | -47.43729 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57af5fc8-5575-313b-bad3-4d44e992986d | -13.14204 | -48.54637 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 105a883f-9a7f-32d4-a993-b8504dce1028 | -7.47457 | -45.81659 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90be3fb6-5842-3073-958d-efabac56a421 | -14.48286 | -43.26262 | 2026-09-29 04:51:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba70e88c-c5a0-33e9-9541-f3918e62ce5a | -12.01473 | -50.93947 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 651ab0dc-9054-3c73-b3ea-501927b627b8 | -13.47719 | -48.61495 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 888ff58d-258e-3d17-9acf-ba94d5d2d018 | -13.21796 | -48.56606 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f34f230-3609-37d2-89b2-1362c13d429f | -12.01356 | -50.96825 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9540ea1-acbe-3e2b-ab94-7d6532bd0c31 | -7.40369 | -40.22536 | 2026-09-29 04:51:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 44cc7e35-0cf5-316c-8b91-49dd803aa700 | -11.41223 | -43.45182 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8e1cf0e8-c51d-3f89-b82a-a370066d9bb9 | -11.3615 | -47.44705 | 2026-09-29 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8373f01f-e19e-375e-9766-f517814d446c | -7.00978 | -45.29706 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b6ec0c0-8a40-327d-bdf5-bf658b0d82d4 | -6.67499 | -55.10851 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9936b186-015d-3fff-b649-1d31acddf327 | -12.90367 | -52.0442 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f03a9e46-03ec-3142-b018-daafdbca682b | -13.37195 | -51.31549 | 2026-09-29 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9439156-454a-385a-8d48-1c9c6f0024c4 | -11.41817 | -43.44265 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82ff67aa-44fb-33a6-a8d4-209238b268d9 | -11.40022 | -43.43523 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2df2bdc5-ed80-3eab-b9a6-4e1622bd89e9 | -11.42886 | -43.46896 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4c5f08a2-417a-31d8-9ec3-b4566c70255f | -11.18415 | -45.13436 | 2026-09-29 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d42d1362-a12e-3643-9662-737685e18ca3 | -12.00853 | -50.97831 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8e77b0d-aa0b-3a06-83c7-23e229cf1211 | -12.31542 | -50.15281 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af2a8148-67eb-3ee5-bbf4-92b32ae63cc6 | -11.18417 | -44.82278 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd7d4ee6-91b9-3a66-a1c9-bbe2bf41a3da | -12.60392 | -47.28815 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ca68094-26d5-32e7-a575-97e4b1435761 | -13.22261 | -48.55898 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3a332dd-ed2f-36e3-9b0e-4a093f1883fb | -11.44808 | -43.46664 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f3c3c7d-108d-3c9c-b7e3-38cf2847208d | -8.85435 | -49.88427 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 493d6e51-1066-398d-b7c9-cb1c7dd1e23c | -11.80123 | -49.05986 | 2026-09-29 04:51:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1ee7750f-ffed-3486-a456-c083a8f91ce5 | -13.34048 | -46.81616 | 2026-09-29 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f3e55f52-b3c2-32d8-96ce-b70ac3b97fa1 | -12.90965 | -52.07138 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 559897ef-5945-3fd6-8fe7-aa4e3739b8d3 | -12.49107 | -44.9555 | 2026-09-29 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef6ef84d-a965-3362-ae9b-6804418578ea | -12.69662 | -47.25903 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5037ada-2e02-3d0b-8e4a-d35a5c80721d | -11.80399 | -50.60783 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README46.md)
