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
| 83aaff78-35d0-31d2-a925-f1a4be39e1ca | -12.08917 | -51.99774 | 2026-06-05 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8913bbf-0c71-3a1a-9f7d-d73c26e5d6f8 | -13.66562 | -47.76008 | 2026-06-05 04:44:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae960b7e-f2ac-355f-8f53-486ef48acf07 | -10.8826 | -46.98817 | 2026-06-05 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7154a157-843c-37af-aa39-8b46a4171ab1 | -10.93085 | -46.96165 | 2026-06-05 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6aa5be3-0df1-3a09-84b4-6128d49422ef | -12.50365 | -46.34535 | 2026-06-05 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57424e21-f3a1-3577-9b3d-a802807874e5 | -11.95278 | -49.30034 | 2026-06-05 04:44:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7011bc0b-79a4-3d5f-a4fa-38a98bd31df0 | -12.08759 | -51.98631 | 2026-06-05 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 372d3d68-5582-3a6d-b5d9-a4a600540006 | -12.44104 | -58.47408 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b75a793-457a-33fd-821b-a436151de915 | -11.99255 | -47.7729 | 2026-06-05 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a46754f-7a10-3219-a20c-7b007676ce97 | -9.08451 | -50.61193 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 891564a3-a611-38ea-8054-0e3f3c0017eb | -14.94596 | -49.55085 | 2026-06-05 04:44:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c421d8e-a64e-3587-8cda-17dcb9cd1034 | -12.00153 | -45.35201 | 2026-06-05 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e24fbfcc-7677-3dc2-8e35-90fac89d981e | -12.43442 | -58.48331 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcdc0a5f-2d30-388f-a337-f5f33784fba7 | -10.14168 | -49.15568 | 2026-06-05 04:44:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f499e8e-8f39-3e68-a7e9-1cb61760a5bc | -14.09504 | -59.38122 | 2026-06-05 04:44:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cfe7076-0eba-394d-95c7-24192c2a7a82 | -10.38527 | -49.44972 | 2026-06-05 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 102d9ed4-e615-347a-a347-9bfe26c1b145 | -12.03228 | -45.88008 | 2026-06-05 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1749aa15-2d48-3cee-89eb-ec4db35df867 | -14.04922 | -53.36488 | 2026-06-05 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd34fda6-663b-3a46-9355-50e1f24b3263 | -11.59893 | -55.33607 | 2026-06-05 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6b65d64-7ab4-3f1f-842f-338b099d8c82 | -9.37073 | -50.54317 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a7b741ef-10b2-3003-a742-fd748851bb0a | -11.54826 | -52.80591 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 496b479f-c8a9-3358-9123-e3bf75306e4e | -12.17833 | -54.53923 | 2026-06-05 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c342640-a364-32ba-8d07-2002c44d8f92 | -11.63807 | -47.87836 | 2026-06-05 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c72ca278-4238-3975-a03c-3c548bdd57ea | -9.09114 | -50.613 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c7d6a89-bcaa-3b3e-bcaf-b07041524be3 | -14.78627 | -50.63694 | 2026-06-05 04:44:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd8186e8-9236-31f1-8e19-d546e9b8d441 | -11.73346 | -56.84508 | 2026-06-05 04:44:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 140a1c76-6122-3531-b29d-2592e6033d6c | -11.60676 | -55.33751 | 2026-06-05 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b44e6aac-d6ab-3def-bd8b-c9d873b6e9a8 | -11.60588 | -55.34259 | 2026-06-05 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e97025aa-d393-3df0-b8dd-7acda957fa13 | -11.9263 | -54.10082 | 2026-06-05 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b16a278-ca3d-3aab-8a8c-fa553e1b932a | -10.86114 | -53.74498 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 959e8c13-902c-3ddc-a58c-22825a7a2f73 | -9.37129 | -50.53968 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e63dabd8-d57c-3430-84a1-5d196617b3bf | -11.63514 | -47.87376 | 2026-06-05 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f420c66e-ffed-368e-9dc9-cee569249fbc | -9.07732 | -50.61436 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 892fbdcc-be35-3fc0-8494-b99d508f6610 | -11.0127 | -54.31354 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b77bf6c-7738-3348-bedb-ad97f016447a | -11.75663 | -47.07956 | 2026-06-05 04:44:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 795cc5d2-f949-339b-8d32-52cbfe961e92 | -11.11499 | -46.00717 | 2026-06-05 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e290224-4e2f-38b1-8568-6333a365626b | -14.37394 | -45.56643 | 2026-06-05 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 763d7479-1a61-38e4-b999-d5f3d78bfba2 | -12.01637 | -55.32121 | 2026-06-05 04:44:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f0922c9-3caf-30e9-bd5e-0e3357b6b62e | -11.63267 | -55.18687 | 2026-06-05 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fc7530a-f763-396f-a77b-66740cb95ec3 | -13.66688 | -47.75138 | 2026-06-05 04:44:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29cbfd19-4d75-3b12-b721-6bbaddfe1ec8 | -11.5489 | -52.80206 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 24259f49-71c1-322a-991e-573da4c1c14a | -9.08727 | -50.61596 | 2026-06-05 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 786531a1-6d74-39ea-8352-0410af7e5ee5 | -14.26972 | -53.24375 | 2026-06-05 04:44:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 607f44c3-cdee-374c-a48c-3d4893ba885e | -9.30288 | -49.92194 | 2026-06-05 04:44:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 008a064e-dfef-3886-b09b-70b5bbabb0b2 | -10.93708 | -46.9446 | 2026-06-05 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 061b8d84-a751-3f54-908e-b74d0c5de61f | -10.32449 | -55.11489 | 2026-06-05 04:44:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d11f8b4-ad24-37cc-88a2-dfb0e784a38f | -11.984 | -57.80201 | 2026-06-05 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c54963c-6b05-30cc-aa81-a80450d1323b | -11.56052 | -52.79616 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 98ab2417-7010-3280-a3e0-7057269afc18 | -11.55235 | -52.80264 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1184491f-350d-3f27-9c55-d93fec902cd5 | -12.73501 | -54.72001 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d83d69c6-766e-31e7-be89-696d4ccc36ea | -12.09095 | -51.98686 | 2026-06-05 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c528f8d7-c4c1-391e-8855-e43094e0459d | -11.01565 | -54.31875 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4be2f4bd-16a7-32f9-a67c-76a7c179f45e | -12.09193 | -52.00193 | 2026-06-05 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9f6ddcf-be09-380c-9345-884918c04164 | -12.41015 | -54.36617 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5373e112-21f6-3b0a-b4ce-3e8cc8a08bc8 | -11.56795 | -47.25094 | 2026-06-05 04:44:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77b649fe-c24c-3023-8752-aa60c6ead929 | -9.93155 | -48.00488 | 2026-06-05 04:44:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07df96bb-a751-317d-bafd-b234572e0e12 | -11.63438 | -47.87662 | 2026-06-05 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ebdab9c-7bf3-37e2-ac05-19ee11b51d5c | -11.45561 | -55.11458 | 2026-06-05 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0fae62f4-f9ae-379d-872f-394be1c16e6f | -10.70183 | -49.6195 | 2026-06-05 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6795d7d-731b-3cdd-b8cc-7ec444a4ee46 | -14.74479 | -52.66476 | 2026-06-05 04:44:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 860d66c8-b1dc-3f20-9689-e2e9d0d72fb0 | -12.30937 | -47.90184 | 2026-06-05 04:44:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48ac2a28-1535-3d9e-a0c9-bec933c7d5fc | -11.0348 | -44.31915 | 2026-06-05 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63d238b7-4f3c-3af4-a75f-d69fa755dce3 | -11.60284 | -55.33678 | 2026-06-05 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45ab4516-9b19-3074-bec1-7a7b50b2d5bb | -11.99611 | -47.77345 | 2026-06-05 04:44:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfc314e8-f2f7-373e-9bb6-e16faea38c1e | -11.55299 | -52.7988 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| db974845-140e-31aa-aa78-4a0307239fe1 | -12.802 | -54.87178 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce31ea5e-da61-3c81-874d-62e053d7605a | -12.09431 | -51.98741 | 2026-06-05 04:44:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 047cbe6c-503e-3858-b4f7-4313739aaf88 | -10.38971 | -49.44316 | 2026-06-05 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0da022de-cd95-3725-ac99-725f6a68e9c2 | -13.51882 | -54.31131 | 2026-06-05 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ba43df3-94be-370d-bd32-82e319fdab6c | -9.90234 | -47.4788 | 2026-06-05 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7af84d4-5ad3-34d9-96fb-3d16e2234e60 | -14.77439 | -52.67376 | 2026-06-05 04:44:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9f55581-fa92-3762-afd6-fe4975c4809c | -11.33143 | -51.39029 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ba94f90-6574-3c77-95b6-37cad2ba6eac | -11.72992 | -56.84003 | 2026-06-05 04:44:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 411170ed-e3b3-384a-a6b6-bf2649cc04a8 | -12.7297 | -54.72844 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98446b5f-b47e-3873-961f-423788ab55ee | -12.001 | -45.35574 | 2026-06-05 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd19bd95-6000-3f9c-876c-9a0549ee4c59 | -12.06045 | -48.07308 | 2026-06-05 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60b9c46b-c819-328a-9ecb-827fa20e59b8 | -10.51879 | -42.37537 | 2026-06-05 04:44:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 36087483-eb91-3249-bf86-014debdea56d | -10.92718 | -46.96104 | 2026-06-05 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ffde58f-dd2f-369f-aac8-5bd4c11e36ff | -12.73104 | -54.74276 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70a41555-7388-30df-9fa2-d10663d30358 | -11.11888 | -46.00773 | 2026-06-05 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e849ab48-a3c9-3ae8-81d8-838510538513 | -14.7896 | -50.63748 | 2026-06-05 04:44:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c62d10b4-33ad-3770-8fd6-7cfa7c3da984 | -12.7289 | -54.73299 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c785cdf2-1030-34c9-80ec-dd645ed73b08 | -12.22541 | -57.27897 | 2026-06-05 04:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f11e7801-cc3a-3127-8622-fc742088f7bf | -11.55516 | -52.80706 | 2026-06-05 04:44:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 30761285-c128-3280-9db5-451f841b5b8a | -14.15025 | -51.59143 | 2026-06-05 04:44:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 694731d6-3cf0-3c44-abf9-a4d7eef383bd | -12.80736 | -54.86326 | 2026-06-05 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b62b3e98-5e64-3d8a-96ea-b4235ffe8e91 | -11.60274 | -49.32472 | 2026-06-05 04:44:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a86088e-4edb-3340-aa99-3efc2c58a2b3 | -12.50698 | -46.3439 | 2026-06-05 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb2284a6-d1ba-3222-9e10-a8695f6cc4b2 | -10.13955 | -49.15558 | 2026-06-05 04:44:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfa43cc8-c34e-3a4a-805e-0bdf5e29158e | -12.43536 | -58.47821 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63462b39-6877-3370-a69c-4ed92909d64c | -12.02923 | -45.88277 | 2026-06-05 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91ee0e75-bbbc-3a80-8dcd-54f695a70841 | -12.2298 | -57.27982 | 2026-06-05 04:44:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49de5c3a-ede5-3d2a-8fdf-607bceca5073 | -12.4439 | -58.48518 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a00a80be-bab0-3706-8284-ad95463c0165 | -12.52498 | -46.27699 | 2026-06-05 04:44:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b327647-3054-3928-b1eb-0be16b6dc713 | -12.45054 | -58.47583 | 2026-06-05 04:44:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac07e65a-2b3e-3410-8695-ab333556d5ac | -14.77104 | -52.67316 | 2026-06-05 04:44:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a28fedff-2280-398e-aca4-1b445c5c162b | -10.60177 | -55.42237 | 2026-06-05 04:44:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a430181-91ec-3866-a2ec-f616845007e7 | -11.38703 | -47.81726 | 2026-06-05 04:44:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec35f5dc-d0ec-32ae-8b4f-99a27a2df979 | -11.00603 | -54.30769 | 2026-06-05 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5730ef18-4127-3a8c-a9cf-b8a3e159b9f9 | -11.60197 | -55.34188 | 2026-06-05 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README12.md)
