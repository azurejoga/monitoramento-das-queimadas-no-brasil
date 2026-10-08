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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 339d0b0f-7000-3b0b-a50b-3b9d6827ea7a | -4.11362 | -54.02305 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca9eeebb-5b67-3e40-9ec1-55ffaca722b0 | -3.07005 | -54.17569 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 111f49f6-8dea-34d6-ba28-7ed655ec0381 | -3.10669 | -53.75969 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba20c868-758a-390a-be6c-e7b3c42a9607 | -2.91141 | -54.10782 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09377f34-ea21-3ea6-a0ae-2e618ec8c78f | -3.28474 | -54.07217 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d190c36d-0cc7-3fca-ac32-bb92a87f6e96 | -6.66689 | -55.09762 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c49ef8b-ba6a-3689-8fff-83ca0f31e41b | -3.01611 | -51.01282 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5bf3efd-8e31-3c5d-929f-bd149d066ec8 | -4.89525 | -54.99314 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cf765ea-f84c-33b9-932b-9462b15a6d4a | -4.07372 | -54.05086 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e81bd315-2224-3ad1-bccf-e901e2b7e138 | -3.58841 | -54.68979 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 532e3a84-6879-364e-ab04-46be724058e0 | -3.32964 | -58.15123 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0375f120-20ef-3480-9f06-07fcaed27d39 | -1.3273 | -55.43586 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 208e07ab-a2fa-301c-b5e6-e0b95416a7f4 | -3.67447 | -60.53699 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e25648f6-8e1c-393f-944f-1348d5c8d66f | -6.12059 | -55.69787 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40a8d9a3-9cc6-3153-89e7-ec8214981def | -2.76787 | -54.8924 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6fa7aab-8cb7-3d9f-8774-21af4a3570ba | -7.38823 | -55.21134 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12684500-0b82-3c31-a675-bf2b0d6599a6 | -2.49608 | -56.30087 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f04e5123-3075-3f19-9370-e74ad2a6b84c | -2.59952 | -57.5843 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c29c4e46-69a5-3bda-8435-0f41f87a0042 | -3.85653 | -55.95647 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdf2bcf8-a89b-3eb2-95d3-96e84223ed77 | -6.13963 | -53.07302 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bca17fa4-d132-3f63-a0da-a50b102e1dee | -3.28981 | -51.56918 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| abc2f2db-e9d0-364b-b00d-3f9c9c4767d4 | -5.68564 | -53.47807 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b2783d8-8bb6-38b3-bb4b-5e75cbe5712c | -3.00741 | -54.09484 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a15728e8-3393-3215-9d41-7e827bb8e075 | -10.2351 | -58.21895 | 2026-10-08 05:23:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23509ef4-f8e6-3014-a189-fa34a7b7fafd | -2.93015 | -56.58858 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cd4b5e9-4f52-39f8-9a08-03249c3c01ad | -1.46255 | -54.6486 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5cb11a54-cc99-3e51-bc5b-b8ac793b8ec3 | -3.02895 | -54.2322 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e0e2847-36e8-3bc7-b1fa-3f3ff5815df6 | -3.99374 | -59.21982 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0d678cd-0829-3795-b861-34f37a19e934 | -2.94844 | -54.16868 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9645b81-c614-3f50-9548-53f9d3118ac6 | -2.75521 | -54.11304 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33f102fb-e3e6-3e76-8123-af011d5898f8 | -3.99874 | -56.25332 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b09ed7a-6e91-3e92-b44e-e2c664c2016d | -11.97479 | -57.58306 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbd8f5e3-5a14-3071-9e07-685aa7108eed | -11.97761 | -57.60932 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d797bcb-650b-3106-a2ee-5878b75d7ba8 | -3.53306 | -54.66648 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 289deb81-bb15-34a9-aa5b-4a4d3b520ad4 | -3.09219 | -53.71223 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 384356e5-3ef5-3f09-bbad-788049e2b056 | -1.45421 | -55.25182 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5fd88ba-5a18-3d09-a0d8-1c79805425db | -1.8211 | -55.22579 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b71377a5-ca22-3fda-bfa4-94edaeeb7608 | -3.36746 | -58.19825 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f557ba46-45fb-3006-b952-4a4632fa6fe2 | -3.3048 | -54.05933 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d0797ec-f339-3c3b-86b6-d5c9f0a5049b | -2.77205 | -54.10298 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86557823-8b96-3499-b387-219b05adfe69 | -3.7365 | -59.45247 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdcdae45-5820-3448-9fab-4bf2c7f8072a | -3.29591 | -54.06993 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31cded44-88f3-3ca4-83ec-0cd13df156ad | -7.23174 | -55.12578 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ac12069d-eed2-3a5f-b4c8-852773468d64 | -3.1136 | -53.78529 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0d661fcd-4382-39a5-b462-69b25098ef31 | -2.95679 | -54.13846 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7114e917-9ef4-34f8-9cc6-ea3681601c4f | -3.23693 | -46.96193 | 2026-10-08 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11e5f1fc-dc33-3e82-9c0b-6877ca547c02 | -2.47458 | -56.07087 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a988ee2-6eaa-3bf7-a3e1-06f62e683f45 | -3.82257 | -55.46341 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7cfcbc4-afa3-366b-af13-784788d5b8cb | -2.99055 | -54.06445 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8441ab00-bf1a-356f-95d4-69e806cfc14e | -2.98935 | -54.0722 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5c689cb0-24cb-33cd-bf10-a89948ffd466 | -3.28413 | -54.07606 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4d712bc-92e2-3997-b7ff-bc8bc559f590 | -4.11567 | -59.88016 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b6943564-45a6-3078-b16e-27af193e372f | -3.10737 | -54.19209 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 141f4328-7f6b-3a7f-addb-01971554fa92 | -3.55795 | -59.47852 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4273b4a7-e42f-37ef-a1e2-8726a7f0a0b3 | -3.86271 | -56.00396 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9a77793c-7ce8-3a31-ae8e-3be6585b65bf | -7.38244 | -55.20248 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70cf6312-da18-3811-a08c-7a8c4a3dcc77 | -3.26026 | -54.04432 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6cbbb264-4909-35fc-bc42-6a2ed22ea2ae | -2.93398 | -54.14682 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50022cc6-594a-36b0-a050-727a17c2dd91 | -2.77425 | -54.0608 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42e6e6e0-953e-33c0-8e62-e961943c03df | -4.42009 | -55.74847 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 349ff68e-f9cf-37d2-9936-54dabf670d58 | -3.16777 | -58.63703 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d81278a-7d65-3894-9fb5-59b92d26958f | -3.71742 | -54.23134 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17045f16-2c88-3abe-bbf7-5549e6bcddff | -1.12804 | -54.11819 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42ea0342-5ed2-3741-8d0e-1092ce1dde14 | -4.06627 | -59.83983 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c7f29192-1c70-33fe-825d-ebb1c02b9889 | -5.23396 | -56.01228 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 796f37d7-2f48-311e-89ed-f79eb4fd6493 | -4.44763 | -54.97564 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 317c551a-2e1b-3713-be83-de627870aa1f | -3.28826 | -54.07271 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa070d19-a8e6-312a-9919-75419d51fad6 | -3.08899 | -54.28743 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af9f5ab6-4f64-3e4b-98b5-60f124da7912 | -3.28859 | -54.02475 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66351d98-9d5f-310c-97fe-690415fbf8a2 | -8.72715 | -45.18276 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9124db52-db4e-349f-8e6c-beaab46c203d | -3.85057 | -51.937 | 2026-10-08 05:23:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba3ca041-dc6a-39c5-a9ff-1d483530ed16 | -3.28513 | -53.838 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d8baccc-e006-3cd5-9779-1871a5f8a366 | -9.13523 | -65.29857 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10cc8046-1126-3301-80e0-76d7732f610a | -3.70061 | -54.20102 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16e8279c-05f7-3e71-9ed3-a05a8c49cc67 | -9.4875 | -64.36322 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 109cc710-9718-3667-8e2b-c373201ae392 | -7.22167 | -55.16777 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 391cebfc-979e-38f2-ac63-2cfd7ce4354d | -2.78058 | -58.46233 | 2026-10-08 05:23:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a08cad69-710f-3a19-9cea-80f5e9a6fe8d | -4.28321 | -55.13136 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0ba6636-4dd8-3a56-a841-85e0f81815d4 | -2.79313 | -54.0826 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbc84d8b-39fc-3b7a-81db-e523aea8b3ab | -3.08026 | -54.29773 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 558723f6-bed1-366c-b17c-5aaf1d6343b3 | -3.20319 | -50.56243 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| afd0fd8c-a5a5-3a0c-a123-32ebbe9c6f1c | -3.26268 | -54.02879 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 142bab69-ce58-379f-94e2-922ff9f66d76 | -3.03522 | -53.91526 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a063810-5e20-3343-8d5c-e2a5a738355c | -2.51372 | -56.25409 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd51a098-ffd3-3085-a4aa-87185cda3b7c | -5.89796 | -52.04368 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7750524f-cf37-3317-864e-a26b45f632ba | -5.29496 | -60.1083 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a199e951-0b75-31d4-8576-f20f2330b1ed | -3.22804 | -54.29637 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 82fb14b1-e94c-322d-a471-ea35603b7b08 | -1.29326 | -55.71497 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e18d1bd-9214-3aab-a805-ae25609fabf5 | -2.57355 | -56.17124 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 65bbab25-88fe-30bf-a27c-765b3ffd73c4 | -2.49968 | -56.14921 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62e347b7-c10b-382d-8425-b01f66a410ea | -3.14434 | -54.36599 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 931d828b-8ac1-3caa-bc55-fa0ad5e4eccd | -5.88768 | -57.75465 | 2026-10-08 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6767f23a-2805-325a-b3a2-60429852a796 | -4.58376 | -54.93127 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e99f5fc0-04b8-3cfd-912d-5b943ee60fa1 | -4.45255 | -47.91786 | 2026-10-08 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dad1674e-397c-3b7c-b194-4ebbd5661064 | -6.06587 | -59.91739 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16b97613-6414-3536-8def-de6dff049c96 | -4.51078 | -54.99248 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d94f9548-c695-3886-8152-4df4446dbaa1 | -4.45207 | -47.9211 | 2026-10-08 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd3aa329-4839-39a8-b0bf-adf7e610737c | -3.58846 | -54.66684 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f0e2d10-d1c1-3de6-8761-7fa263756182 | -2.38995 | -56.13555 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab7a6a8b-67d3-3e19-a5d6-53abafd2eb2b | -8.62019 | -66.99969 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README168.md)
