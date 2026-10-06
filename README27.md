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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5c8626d-2375-3afe-a80a-8cf8c9c18cfd | -6.00591 | -47.40236 | 2026-10-06 04:19:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5309b258-dc20-3d5a-8218-7f2422eb9b43 | -8.74172 | -47.87924 | 2026-10-06 04:19:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e51e0c1-2e20-3fb6-91e1-cffe3300ab58 | -5.43853 | -43.44436 | 2026-10-06 04:19:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9a3be059-e0ad-361d-9214-bec2fdf4ed08 | -3.15555 | -50.44659 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f234e78d-fb49-3f64-b82a-601c5554664e | -5.61209 | -44.8409 | 2026-10-06 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79b14c8d-5c73-345d-aac0-8942b8dcd470 | -6.88393 | -43.67854 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b96f017-3979-386d-b721-60c70edd7628 | -5.03239 | -43.57148 | 2026-10-06 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56890475-2661-3644-bef6-d196a963f1ab | -6.91126 | -43.66357 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18dbb122-d624-37bd-94c2-903c2128ce31 | -3.11694 | -53.70784 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 177ff346-568b-3b12-940b-06f088f8046a | -6.15381 | -47.1205 | 2026-10-06 04:19:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc0a2376-6ddb-31e8-b869-a5fa35e335ed | -7.10279 | -42.53697 | 2026-10-06 04:19:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e0552558-e66e-39da-b88f-1b2d38904aae | -4.2847 | -50.26864 | 2026-10-06 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2e93136-130f-3673-884b-96cb8f088d6e | -3.09208 | -53.72908 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 53d1a382-886d-3726-99db-e4f3eb7b120e | -7.24652 | -45.26422 | 2026-10-06 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 214e866b-c5d6-32c3-87b0-05463bda8ad3 | -5.96459 | -41.35605 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c686c2c-64c9-339a-b53e-fb6915e123a1 | -11.27153 | -45.50971 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 3b888f55-7237-37c1-91b2-2d8575083a08 | -2.78515 | -51.67073 | 2026-10-06 04:19:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5bd20000-1cd6-3f04-bed6-304f58d0959d | -4.4593 | -54.96329 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 23fbefc7-7d33-378b-81a4-ff950fccf219 | -3.83738 | -50.3133 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf2040cf-c020-31bb-9ccd-c75821d14f33 | -11.26298 | -45.51674 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89fb25a8-8c1e-382d-9c3c-bcd872a506cb | -6.92389 | -43.67343 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2e1e8a9-340f-31d2-b62e-357e0a215a8f | -2.9893 | -54.12141 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9161f090-e08d-34f5-9c13-8138749ac300 | -9.14247 | -47.98371 | 2026-10-06 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 621000d5-fe67-3eac-b2a3-7cb251b5a251 | -7.203 | -44.31143 | 2026-10-06 04:19:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de428828-dccb-30e6-ae21-b9f3c5f6a873 | -2.77647 | -54.08796 | 2026-10-06 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a90f1b0-0dfe-39e0-bf2a-3068a116ba25 | -6.92861 | -43.6781 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0a5affb-4c08-369b-b592-5e3e3a94ca0c | -2.92976 | -54.13128 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1be230e-4a88-39c7-87a9-de642c101827 | -2.77795 | -54.1061 | 2026-10-06 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33ec525f-d842-3b79-89cf-d1daea725ba7 | -3.05877 | -54.22932 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32806a9f-8a48-3b11-a76f-b375b2af0c2b | -7.47991 | -42.80171 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 90e16e9a-237b-3968-8398-b40a451f4490 | -11.27443 | -45.51447 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 83885349-d214-3706-84a0-bfebb0ec69c8 | -3.12377 | -53.70905 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1db06d8a-001c-3a26-9c37-441666109f0e | -6.66845 | -43.82581 | 2026-10-06 04:19:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8c49025a-a32e-38b9-990f-ad40150ef10e | -3.06657 | -54.24682 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 586f3ce3-ebe5-348d-976c-f4463f4d0cb2 | -3.0874 | -53.71556 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 02582a6c-c070-3ed3-8798-ec52a409048e | -7.02035 | -43.44229 | 2026-10-06 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40351342-a44c-3d61-832a-62a353f9872a | -4.6524 | -42.44743 | 2026-10-06 04:19:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| afc7fece-10fe-3773-b18e-01ba388552be | -7.88296 | -44.19164 | 2026-10-06 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46fbeb34-0888-31e0-a0d1-f08a4d36203b | -7.01692 | -43.44174 | 2026-10-06 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d363b6c1-163e-344e-80ee-e6acbbcbd1d0 | -6.34776 | -42.56596 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 41ae710b-3890-3062-831b-1a02eb7ce971 | -6.35004 | -42.55169 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a1585f4c-1ba3-31f8-898f-8de362ea443d | -3.09425 | -53.71668 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c30b6534-401d-36e1-97e6-42795153d264 | -11.2787 | -45.51096 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| af5572c9-63c1-3db7-b747-38139ca3cccf | 2.45507 | -50.8438 | 2026-10-06 04:19:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 07db8159-04f0-3cfe-8454-39e401edaa65 | -2.87517 | -54.12988 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f7ab4746-c095-37eb-a722-e8038f314b02 | -3.16231 | -50.44059 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e1335658-2338-3ae7-8158-70e121d7a68a | -2.87705 | -54.14269 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 69de78af-9524-344a-9cad-49633bbb8a19 | -3.0976 | -53.73547 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f8df2c7c-50ed-35d9-92d7-45ac1cf38172 | -11.63076 | -43.61979 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 892319de-e2ca-3eaf-aab7-5aba982545c4 | -3.05494 | -54.22994 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc6506d5-7f0d-3f3b-b06d-d35b35aab835 | -9.86408 | -44.80997 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e664eea0-b75d-33b8-9a41-ac33ce9b8f05 | -6.42162 | -43.46597 | 2026-10-06 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceb09597-f3e6-34bc-9a19-a83b7605f8a4 | -11.27222 | -45.50557 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a7a0c816-e6fa-3d77-9ac0-f716336a54b5 | -6.82415 | -39.30457 | 2026-10-06 04:19:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 895087bb-f56f-3de5-a73e-dfbd18d7835e | -11.6524 | -43.65643 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 881f8a08-c5cf-3524-bd2f-c2c6929a831f | -5.4086 | -44.35066 | 2026-10-06 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4e332de-db97-3057-9bbd-eaf009359c21 | -9.92496 | -48.14035 | 2026-10-06 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b51b2e9-8605-3bfb-9b6c-4f2fc4dc9105 | -3.00567 | -54.13865 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1e6e0bbc-e0c5-30ee-9a6c-8ef129f3363f | -7.53278 | -45.87759 | 2026-10-06 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 371e1aaa-708d-31da-9840-97b4f223383a | -11.2758 | -45.50619 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| df200f32-fee5-3f89-bd60-281aa9ac5daf | -5.40682 | -39.10566 | 2026-10-06 04:19:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a426d898-766e-3b28-88f7-7685de23ea64 | -8.30241 | -45.46877 | 2026-10-06 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cd74d15-8458-38ab-8126-580c6df997fd | -6.81951 | -39.31154 | 2026-10-06 04:19:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a41451d2-3ab0-3126-9604-a1a90ebf853c | -11.64568 | -43.65535 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f05f8774-8e4a-3fa4-8b67-7a6df112cbaf | -11.26437 | -45.50846 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 2875a13b-3890-362c-ae97-76246209c550 | -3.23582 | -53.87368 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34a7eb3c-812f-3df3-80ca-2dd6e1bcccf7 | -5.67053 | -42.58646 | 2026-10-06 04:19:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8094c08a-f33c-3723-aa95-98fda40baaa8 | -3.05021 | -54.21534 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dab171ac-8213-3f94-8e8f-0ddd2b673aec | -5.95124 | -41.31125 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6926107d-8e03-3761-960e-359d7ea5593c | -3.02066 | -53.89231 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a239e6a4-1083-3f75-9d9b-4587176b57f5 | -3.12196 | -53.76012 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 943895e6-890c-3ff5-8a33-da747fa4846b | -3.495 | -49.90059 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abb37e04-8bd8-3601-8f3d-e5ad75fc64c4 | -6.60891 | -41.58267 | 2026-10-06 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c7f418ce-6ec7-3035-a8e2-b5d46e3466c6 | -3.0204 | -53.89788 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| eb4cebd7-af39-3b11-9f4d-57058df3d167 | -5.61138 | -44.84524 | 2026-10-06 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3e6f22d-668a-3f6e-9a52-088f1e3e68bc | -5.41243 | -44.35039 | 2026-10-06 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31908b04-c80b-3c1a-b4c0-f17b7343f2ca | -6.42445 | -43.47031 | 2026-10-06 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baf15c02-5c00-30bb-92f3-89c4dde5658e | -11.63193 | -43.61261 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4693ede4-028e-381a-a3e4-cd59ff4c76c1 | -6.67256 | -43.82255 | 2026-10-06 04:19:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e9b14d6-3de7-3bec-867e-8b523aad794c | -4.23737 | -49.98077 | 2026-10-06 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c82081b2-9af5-3955-87fb-770d708ba17c | -4.51079 | -43.69689 | 2026-10-06 04:19:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c10f27f-8f2a-34d3-85aa-2f64bc4c6b60 | -7.82679 | -45.56109 | 2026-10-06 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d46b70de-7cb4-389b-9a30-052fbd47fef8 | 2.45433 | -50.83895 | 2026-10-06 04:19:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d0a53514-decf-31f8-b478-130855495a73 | -3.22893 | -53.87251 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8614eafc-bae9-3ae9-907d-9dcbfa57bd0d | -6.92328 | -43.67722 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d9eeb631-b7f2-3e10-a69a-eb80279729d2 | -7.25983 | -48.06792 | 2026-10-06 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9656b02a-9786-30f2-b79c-a9a3577fbf34 | -4.45602 | -54.9752 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 311ad22a-a931-3db3-a3ee-b1764924926c | -7.24428 | -45.2548 | 2026-10-06 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31712001-fdfc-3671-897a-a048a6e8a092 | -9.95143 | -43.4815 | 2026-10-06 04:19:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b15a4f1-8c98-3caa-ba0f-55908588e684 | -7.46994 | -42.9992 | 2026-10-06 04:19:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8bdece54-4d6e-3155-ad87-b33e2ecb7188 | -3.16845 | -50.43815 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aed09b12-5a17-3616-a01e-5b611cccca50 | -2.8036 | -54.14139 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d83eac8-aeb8-3c89-b679-97a8ee972933 | -7.15034 | -39.54047 | 2026-10-06 04:19:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2a30c517-1f0e-36ba-b83a-39cbab1b5362 | -6.00229 | -47.3975 | 2026-10-06 04:19:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9a5747fa-7199-323d-982a-545b175eeff7 | -4.33627 | -43.81403 | 2026-10-06 04:19:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 835dcacc-d89e-3961-9cbc-0431e436e68d | -6.92577 | -43.67376 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 990c988b-cb49-3f11-90ee-ac2b3c8328d1 | -11.27952 | -45.51379 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 922ce53f-a5fd-3907-bf7e-e521fc03922e | -2.77914 | -54.0994 | 2026-10-06 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 54280b57-4833-3dab-bad4-897743ac4d81 | -8.60644 | -45.66131 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dbc228a-59ae-3be3-9551-321897285969 | -3.10074 | -53.71682 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README28.md)
