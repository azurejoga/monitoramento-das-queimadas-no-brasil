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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7687b099-52ed-3feb-b545-c2f4c0ef4075 | -5.85765 | -53.45246 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9716ded-ce1c-335c-9c0f-f2dcd429bca6 | -3.29113 | -54.08009 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f1a5e0c-89b3-3b27-ba49-9001fe4c29e7 | -3.25797 | -54.02 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 140accf8-c201-347f-8d7e-84f75d7717f1 | -6.48715 | -62.8659 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8764bfae-68a8-3cb6-8aa4-64a0d60c945f | -7.00266 | -59.10058 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79e26f3b-85e5-3665-b6ab-10383ff44760 | -3.96298 | -60.002 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a61ba0d5-9fdc-30a1-9eb6-675c467646e8 | -6.00611 | -40.96333 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d816e95b-593d-320a-9d61-676fdb1abc71 | -3.56324 | -54.67074 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f0b271d-de2a-386c-b450-91844f520209 | -3.07777 | -53.94994 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05e3cbe0-c2bd-3c97-841f-c975fe2fae52 | -3.74788 | -59.47075 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 517d1075-b8a3-3273-b4d5-d1689a4a332d | -3.02296 | -54.09008 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b84cdc48-278e-3142-ac85-1df2b3fd7f31 | -3.94356 | -56.02323 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9fe8845-ec6d-3e53-96a2-3b4723d83e58 | -4.57548 | -54.9559 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7270c6be-31e6-3970-b784-0e1e35026f91 | -6.00118 | -40.95296 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d34a729e-1bff-37ab-aff9-04f2d4bc5608 | -2.98641 | -54.76897 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 179ff516-0dc9-3a49-beb8-e996b61b8642 | -6.68339 | -63.02865 | 2026-10-09 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 585e8250-af9f-3078-b117-6479ad8de605 | -4.29785 | -60.01606 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee936374-16d1-310b-b4d3-76a80808495b | -3.27966 | -54.06254 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0f2e599-b8eb-369b-aac1-2107f137e68c | -2.9617 | -54.15658 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc4edf31-5b51-33fd-b173-5d5077c1d6a2 | -11.21271 | -45.25315 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87b59976-9496-3cd4-ad64-40bcdcfb7b79 | -3.01597 | -54.08897 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fefccbda-054d-3546-ba9b-6edd77f3a300 | -9.04867 | -47.73875 | 2026-10-09 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1f58e13-94bb-3264-bd58-f5080e78c3e1 | -3.926 | -56.03477 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8bcd70f2-66e1-3a3a-9100-24ed2a91fb47 | -2.85673 | -59.12073 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c65a59b-bbe7-3fb5-a2d2-b16a6abc1dda | -3.73766 | -57.12767 | 2026-10-09 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9615612f-aaf1-3fd7-a1ff-4737b43ed42e | -6.07064 | -53.60363 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afc28d0e-ac59-3fcb-bac0-c625f9639da1 | -3.20927 | -58.84378 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 560ca290-4693-39ff-8d52-3dce820be23e | -11.58187 | -43.65257 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d3ed2e7-c7b1-39eb-a619-9f8ef54ece02 | -5.82596 | -53.5421 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 860e382b-fee2-3f3b-a2d9-4f2450d76d0a | -8.4368 | -47.03143 | 2026-10-09 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aefbfdd9-0b7b-3c3b-89ab-57d11016b220 | -3.06123 | -53.92004 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b5d0f8d-e236-3d69-9101-ad1e4da8ae44 | -6.39227 | -55.26676 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d75b296-9d09-343d-bcd7-343758dcffa6 | -4.41715 | -49.66152 | 2026-10-09 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce46535d-06eb-3c46-8474-074cfb892b09 | -2.99297 | -54.77427 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b013a48d-288a-3c21-aede-3d97aab14b5e | -3.43283 | -54.54561 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cf64800e-b7ab-33cd-8722-97841a728282 | -3.09219 | -54.28712 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f34ff19-c08f-3b69-b640-025c8bc91ce3 | -2.99789 | -54.76659 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e24a9fd-929f-3a52-89b1-6d9e73c09436 | -6.16629 | -51.93538 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d615a39-7102-383a-8e66-0a794fdee761 | -3.73053 | -57.14524 | 2026-10-09 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63f7069e-0d96-3284-b790-282752ac10a9 | -2.81221 | -58.29164 | 2026-10-09 05:04:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ac606385-d3c7-3349-893a-74211172fa87 | -6.01039 | -40.97842 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| d797d05d-12a3-3976-979a-ba06a14194dd | -3.57819 | -59.07433 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3b23487-eb47-3993-907b-41bca7654880 | -6.01109 | -53.49197 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| effc562f-fd07-30f7-b440-61c275a459ef | -3.31389 | -54.70485 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c83ae8f-24c3-3a20-a9f5-5f41cb97b954 | -6.92138 | -59.27733 | 2026-10-09 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6af5d801-a3f6-3dc6-812f-6562afea34c1 | -6.30916 | -54.80746 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5235cfd-7a79-308f-b8f4-2db5bfbb3804 | -3.07726 | -54.28974 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f35ad514-830b-3b88-b629-7245a11136d7 | -6.01928 | -52.76291 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8da62f51-6827-30f3-b0f2-5167182d3d57 | -3.58549 | -54.31512 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c54a268a-e1f1-366d-8ee5-f717789afa51 | -6.90122 | -45.88929 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a8141c0-bb84-3283-9e83-12a0d977a8b6 | -4.29566 | -54.80582 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 473f3806-5b50-3d2d-a8f3-7542ca41a72e | -5.18916 | -46.22074 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05a1fbcb-6508-3bdf-a9e0-bc2a971b621f | -7.82012 | -44.57017 | 2026-10-09 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 541eefb8-deb5-3985-8ca1-d624a5ca3687 | -5.6997 | -53.4533 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38e93463-50e1-354f-a336-c6ce87476bb5 | -3.18479 | -58.64517 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a847a354-dd42-3d77-b9ae-58675cf4b0e9 | -10.32118 | -46.61069 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07e1c167-b4b9-34cf-946f-58c46723125b | -4.12408 | -55.02655 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38bf49ac-26b2-3043-96e4-f693e3be7913 | -3.03918 | -54.1006 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4720f480-fb43-3aa7-8cb5-4400bc176c2f | -6.01558 | -53.48544 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 056dc1f8-5bdf-3f1b-b2f9-b7d8964fef5a | -2.99564 | -57.75042 | 2026-10-09 05:04:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cf4357e-efe5-33b2-907d-b37109a3956e | -6.49713 | -55.30823 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89d75146-e6c0-3d5f-b9fe-f7eecfffdcb0 | -3.05391 | -54.20998 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22b3787b-786e-3485-9317-6655d15e1586 | -3.43217 | -59.53843 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 299d4a8a-9c1a-3439-9b34-100b55e48155 | -3.11705 | -53.79377 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3afdeda0-abfe-3edc-a249-2e17fe0317d3 | -8.19638 | -46.42226 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f9d6ebf-5afa-34ec-af90-76480a88ede7 | -3.06939 | -54.24845 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af5abba1-8f9f-39ea-9cc4-e59dd2170cd6 | -8.70109 | -62.41602 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13f7b5c4-32a9-324f-a2bf-a6e3da02b38f | -3.01211 | -54.06866 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ce6b6ff-1168-336a-a6dd-5a39c1936223 | -3.92677 | -56.03004 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d4f39a39-1cd1-3fd3-85f2-f7fa4c8333c8 | -3.30378 | -54.02347 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32ce1cc8-10e6-39e4-9451-d1943899b749 | -4.66897 | -56.21252 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f69044d-9903-3ee1-aee7-7088b61de035 | -3.0267 | -54.06704 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72380433-d6df-3c88-81e5-b4ce81066fbb | -3.11755 | -54.17559 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49e81d37-2afb-36b1-8609-141c90aa5006 | -6.11729 | -55.68422 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b86a6831-eed6-3909-9cac-51791aa757c8 | -3.53248 | -55.43478 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16bee612-f856-3d2d-a0f0-e1ac16f47c0d | -3.30604 | -54.0316 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 596d4104-0016-3336-8d4e-765dd016c11d | -3.65455 | -54.28909 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc78d1d0-375a-3cce-a253-9df15b4b22c2 | -3.92904 | -56.0401 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 52a30702-0f10-389c-854f-2bf8afb8a511 | -2.99564 | -54.07878 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec1c2707-02e2-3045-9810-8bbc9444773d | -9.13157 | -45.8478 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1b384b7-d4db-3764-bff2-271496c65281 | -3.40207 | -60.8489 | 2026-10-09 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c0c57c4-c52a-3d85-ab8b-e1f545a1dfd0 | -3.06094 | -54.2111 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e1a5f9b-354b-33b1-845c-594a8287f1da | -3.532 | -54.67118 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c8e6a05-4a03-3942-9520-66dc18493857 | -3.12042 | -54.18004 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b64e40d8-7ade-371a-8e18-6791d0912627 | -11.53262 | -47.15075 | 2026-10-09 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8775bc15-2b94-3997-9217-9c06f09b38fd | -7.44693 | -63.55236 | 2026-10-09 05:04:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fde5befd-2840-3430-9a26-22b30adf24db | -2.98142 | -54.03321 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3b3ad35-168b-3291-997e-859588827e7e | -4.55142 | -54.96856 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 86f4488f-40a5-361d-a1ab-0ccdd5c46275 | -3.05034 | -54.03156 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28139c68-df25-3f59-98d7-10d46ed4dc84 | -9.16403 | -61.4086 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e035c34-66b4-397d-8d8e-c4d6b04ef9e4 | -3.1154 | -53.78194 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47f3fbd5-9d8d-3e24-999f-46890c590a3d | -9.9078 | -44.78494 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f963521d-f028-3a3d-96e1-1231d3812d70 | -4.0564 | -55.32973 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4becf1a7-7759-39c5-bc60-6a5016610097 | -6.70105 | -47.38505 | 2026-10-09 05:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20f27097-3d35-39d0-9e49-06470b047bdb | -11.65339 | -43.67893 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d797071-e4f0-3261-b751-49ff603298af | -5.88515 | -43.41795 | 2026-10-09 05:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d39ddd7-5f34-3d50-94e9-e85778556bdc | -10.20431 | -47.68351 | 2026-10-09 05:04:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 462da70f-5b7c-3ac3-acc9-c43e056b6fae | -3.17983 | -60.39375 | 2026-10-09 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 653fe524-2e2c-38d6-a7db-a8974a4ac38f | -7.57343 | -61.54122 | 2026-10-09 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a08725c5-9589-37c5-b371-0af92e4caca6 | -5.89614 | -52.04621 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |


[Clique aqui para ver as próximas entradas](README146.md)
