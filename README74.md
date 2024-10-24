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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3911dfe9-82a9-3de6-913b-09b12801c813 | -5.62082 | -44.83657 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6365ccc1-c732-38f9-b50a-6bd0f145dc55 | -5.61964 | -44.8292 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5173d6df-12f6-3a53-9f90-db2cf850203b | -5.61917 | -44.83258 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3e0c2976-0b26-3774-ba09-88aff2839306 | -5.61646 | -44.82903 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ddd1b3f-f23d-3a0a-ba49-1027337338f9 | -5.61597 | -44.83239 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1eb5f7ab-087b-383f-a556-5920291644ef | -5.6092 | -44.87889 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8278c05-1216-3720-ad8d-fe22bae394bc | -5.60872 | -44.8822 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da1d1902-deb5-3b61-be2f-dac6b2c76004 | -5.60741 | -44.87841 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f487d0a9-5604-30c0-90b9-9d561b5f333d | -5.60696 | -44.88169 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cc6ff8b9-f5a5-3b80-9b11-3f64c88995ed | -5.60387 | -44.87812 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7c7aaa92-87ff-37ed-949f-5202bcbfcff7 | -5.6034 | -44.88138 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 68db4cfb-5d5a-378f-8b14-918c6bcdc96e | -5.59851 | -44.87755 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9298d831-df58-3966-bda4-fe8bc9157f11 | -5.59804 | -44.88084 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1e4f1e21-0c11-3c49-a6c0-d8f0211e1a26 | -5.58594 | -44.88928 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89f754e8-ddb7-3e63-811c-8c20e64bd5ea | -5.58199 | -44.87896 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9aee10d5-15f5-3dad-b2b5-3a8be6850a8e | -5.58152 | -44.88219 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8af5c052-c360-3998-89c4-475a5207cde2 | -5.58106 | -44.88541 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 65ec6001-4d6c-3b96-aaef-1db723e3b818 | -5.5806 | -44.88862 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 385763a3-0f2f-310a-9c2a-a54e8cbf6636 | -5.57573 | -44.8847 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5c721c2f-3af9-374e-95a6-8a2d40350937 | -5.57526 | -44.88792 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0bff2514-c9f6-3777-8f4b-999e6ee1e8ec | -5.57481 | -44.89112 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| be716c42-0df4-38ee-a20d-679666ca6481 | -5.42768 | -44.79496 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 999ce8ad-e880-3099-a0a5-211a5d2b4a2a | -5.4244 | -44.7947 | 2024-10-24 04:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6547b551-6334-3d1f-9ac9-915f26653932 | -7.4312 | -44.73218 | 2024-10-24 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81182dbe-510c-326e-aab9-275e06c4e91a | -7.42569 | -44.73129 | 2024-10-24 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e4d297c-1537-3ca5-9a64-c370afde1d6e | -7.4252 | -44.73488 | 2024-10-24 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0c78a0c-119c-3de6-a978-0e1262502688 | -7.41513 | -44.72614 | 2024-10-24 04:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e908dbc-e826-32b8-98d1-3293127f2a6e | -7.1756 | -44.99858 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af0b51f3-3bf6-3197-a1ea-d7a2e7e45c7f | -7.15056 | -44.81777 | 2024-10-24 04:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c4e01a3-f1c7-3d23-af68-1ca2911ae750 | -7.01523 | -45.02715 | 2024-10-24 04:55:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 587f63bf-6614-3e33-b359-aff9f90eed47 | -7.00984 | -45.02644 | 2024-10-24 04:55:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fd99dc0-e0cf-3967-be50-1a22e328b181 | -7.00936 | -45.02992 | 2024-10-24 04:55:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 678633a4-1d34-3119-9630-fa144134fc95 | -6.88158 | -44.31966 | 2024-10-24 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 748b4acd-be0f-3410-b243-ddd1261f7ef7 | -6.88111 | -44.32317 | 2024-10-24 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f6ca630-4c68-34c4-a0d9-292db8875c67 | -6.83014 | -44.383 | 2024-10-24 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9699d11c-6745-3c11-a889-7c1c78c437ba | -6.82962 | -44.38671 | 2024-10-24 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fbf2cdd6-739a-3486-8705-9b8dfe8887ac | -6.8245 | -44.38244 | 2024-10-24 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea9a9333-8820-337a-93bd-3d0a695b6c78 | -6.82398 | -44.38615 | 2024-10-24 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c0c19db-a656-377f-81a8-960a6eaa8d33 | -6.81238 | -44.46962 | 2024-10-24 04:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 838b3e30-d3c6-3b0a-a601-6f31b95ef5dc | -6.72099 | -44.68343 | 2024-10-24 04:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a16256f9-786c-3c3f-8d0a-bd1a45a533c2 | -6.72072 | -44.68235 | 2024-10-24 04:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 763c87ca-0a53-3a19-99d1-ec7a20678d0d | -6.72051 | -44.68698 | 2024-10-24 04:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50b6585c-bdc9-3dad-9de5-8a96b380a9f2 | -6.72021 | -44.68589 | 2024-10-24 04:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bab233f-4220-38da-a450-7b3dd9697860 | -6.71971 | -44.68941 | 2024-10-24 04:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e1f4252-17cf-339d-8f52-ba41faaf93c5 | -6.58842 | -44.17721 | 2024-10-24 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b695a97-52a6-3747-a29d-586b55023279 | -6.58791 | -44.181 | 2024-10-24 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bdccb55-49d0-3539-a24a-3270b7c3c4d9 | -6.5827 | -44.17685 | 2024-10-24 04:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19f1e690-14c6-3481-8588-fafe00719e38 | -4.58 | -45.61065 | 2024-10-24 04:55:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a19c65ae-80b6-32c7-987c-1521fb11ce8c | -4.55258 | -45.8002 | 2024-10-24 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dbf8635a-d776-33dd-a2a9-45c74c15027a | -4.55177 | -45.80577 | 2024-10-24 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff051627-a513-3810-9328-47450d6befd7 | -4.54765 | -45.79949 | 2024-10-24 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 42479c60-bd1e-37c0-bf55-0498e7c44086 | -4.54271 | -45.79886 | 2024-10-24 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ee4354f-8730-3881-83ca-7ff69b40c1de | -4.29497 | -45.99713 | 2024-10-24 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa96e6ac-b9b3-3cb4-8229-e899307903bb | -4.29219 | -45.99556 | 2024-10-24 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1867070f-11ec-3659-8154-7bee1f928ba0 | -4.29141 | -46.00071 | 2024-10-24 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3036be44-567c-3cc6-912e-8cf6946973ce | -4.29014 | -45.9963 | 2024-10-24 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d940296-3c2b-3773-b455-045b9698af97 | -4.08983 | -45.51388 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| a4d361d0-a014-396b-a9f0-dda2f365cf0e | -4.84929 | -45.85432 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f409b19b-9e2c-3475-a863-3b028a703c55 | -4.84585 | -45.85495 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1870a68-0164-3211-9baf-3abb9e5a0f0b | -4.84435 | -45.85373 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 158d5ce0-3cd3-38aa-bf1b-27dccd11e517 | -4.80303 | -45.6881 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d30e2e16-4e92-3b8d-9d70-a4bbd7a479a2 | -4.80219 | -45.69384 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1fad2da-e0e9-33c1-b429-776108b915f7 | -4.7972 | -45.69317 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3293ceef-2f16-3e66-8854-662844d1d5f7 | -4.7964 | -45.69867 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cf048510-181c-3741-8c7f-7004d60e8343 | -4.79301 | -45.68697 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28277ce7-f0ef-3168-adeb-b5cea9f59884 | -4.79221 | -45.69248 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a64fc3ee-60ec-3a11-bc40-75a76ddb9039 | -4.78804 | -45.68616 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74865526-6a58-3462-ba8d-916c112a2012 | -4.78723 | -45.69174 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2c0e58f-e161-3ff6-aae0-a398cfe924f7 | -4.76754 | -45.75802 | 2024-10-24 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a334cbd-ab62-3fb5-a052-8222bbf6ea22 | -4.76258 | -45.75728 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67d4eb4d-3159-349a-99da-7c645ee290d8 | -4.76177 | -45.76291 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb5f9203-a1e7-3a7f-a2d1-deabec67fac2 | -4.75604 | -45.76764 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b3fa99f-ecd5-394b-8387-502ff9416b4d | -4.75493 | -45.66854 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 799ef8e7-3468-32cb-93a6-fc980519c879 | -4.75038 | -45.66721 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e738dc5-a868-3162-a73d-aa4a13c03fa6 | -4.74993 | -45.66789 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56063d01-f0ce-3ca9-b7da-2f3a41fa95c6 | -4.72046 | -45.73168 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e8d09a4-be95-33df-946c-17ff1fddfd8d | -4.71472 | -45.73625 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 425ace18-5815-3ca3-a04d-b017ce4a1394 | -4.70977 | -45.7354 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0bb5cd02-69e1-3eb4-a83f-48573cff3ae5 | -4.70898 | -45.74081 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9f7f0452-1833-38b2-b7e8-e6d4f9aabdab | -4.67921 | -45.80595 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cae19330-b1d2-3faf-b2af-e8d4b9edf547 | -4.67841 | -45.81148 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5879fffe-ead5-3726-9087-437040282789 | -4.65584 | -45.68761 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f2a54b23-00c7-3f3f-a448-28f2bde17bd6 | -4.65556 | -45.68506 | 2024-10-24 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f3a8c24c-1d10-3200-b0c4-168ef965f049 | -5.08527 | -44.92513 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f3feebd-51dc-3fe3-8c7d-2cdc5e20023b | -5.06425 | -45.50449 | 2024-10-24 04:55:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 915bb637-ff19-3577-8d9d-99de00b8da90 | -5.06381 | -45.50748 | 2024-10-24 04:55:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efd70004-f805-3c2e-8bf5-94b6caa52cb1 | -4.96667 | -45.51365 | 2024-10-24 04:55:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e7ab4c1-8367-3424-ae04-b9e1e6a0ffc2 | -4.96159 | -45.51307 | 2024-10-24 04:55:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e736fba-5061-3dc0-9f1c-58b52976a216 | -4.96115 | -45.51606 | 2024-10-24 04:55:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fa6a539-42ed-34bd-8a95-0e70a7260d0e | -4.84992 | -45.03457 | 2024-10-24 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6e41e83-e17a-3359-9682-9251e57d4ae7 | -4.84978 | -45.0346 | 2024-10-24 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7f0598d-849e-3f28-86ec-a1e602cf93ea | -4.84944 | -45.03778 | 2024-10-24 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 254f60e0-7dcf-354e-9b49-ec436ffa91b8 | -4.84933 | -45.03782 | 2024-10-24 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5511b6ea-6898-31fd-a6d6-ff7111a51a58 | -4.84471 | -45.03374 | 2024-10-24 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65760b6a-5bff-31ba-8acc-9620213bd952 | -4.84457 | -45.03376 | 2024-10-24 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47fdf966-e349-3f97-840a-fc828d7397eb | -4.84423 | -45.03695 | 2024-10-24 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 293e053d-2a2a-31bc-9528-378e32688016 | -4.84412 | -45.03698 | 2024-10-24 04:55:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3718409a-260e-3581-9b32-676dac26a3b7 | -4.08484 | -45.51316 | 2024-10-24 04:55:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1950dedf-b86f-302f-b016-d8f17029efd9 | -5.7089 | -45.0038 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0960dcf-38ac-370e-b26d-a6ac41592824 | -5.70795 | -44.99829 | 2024-10-24 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README75.md)
