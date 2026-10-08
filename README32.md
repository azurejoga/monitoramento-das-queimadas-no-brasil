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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33e8df42-ee23-377c-b6fc-77aa3f473356 | -2.7163 | -57.463001 | 2026-10-08 00:48:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab6b36ac-6798-36c3-b43f-4b2d3991df80 | -3.5729 | -54.662102 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26355d92-b9cd-3c5d-a54b-a3e38f6d30dd | -10.4314 | -47.265499 | 2026-10-08 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3faa7c52-4c4e-36cf-b162-38058ae16f76 | -3.5294 | -59.491402 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d317453-40c4-37fc-9e84-3c7bc8dc57ef | -3.0069 | -54.753101 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d73091c1-ccbd-312f-ba76-885e3d00acd0 | -2.4618 | -56.066898 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 074683a3-ed10-377c-8a9b-7c13ccf30f6d | -2.9253 | -54.077499 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f9eb3d5-c9d6-399c-8996-e2a9567e608e | -3.2724 | -54.0639 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cacafeaf-5ee8-324a-8ca0-a0d1301a3a3a | 4.0943 | -60.5797 | 2026-10-08 00:48:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9ad7d6fa-8bed-3755-9c93-aa6f2aeaf305 | -4.307 | -50.791199 | 2026-10-08 00:48:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11353c73-c83b-3488-8791-d5bfa91a1a2d | -1.528 | -54.814301 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b66089a-606a-36f6-9f6f-bf6f7ef9bd99 | -2.9552 | -54.118301 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec5cc6b-80b9-30db-befc-53f71ed81466 | -2.8175 | -54.101299 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 335f29b6-0f08-3f94-b1d8-b1e457d3c4e6 | -2.8855 | -54.173599 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e457e6e2-e1cd-3655-872b-be16faee4127 | -5.7335 | -45.155499 | 2026-10-08 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0740d01b-fa6b-335d-98c9-aeefcaeb3351 | -6.1043 | -49.418098 | 2026-10-08 00:48:00 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50ca9d88-f734-31b1-a9bf-baf4aacb69be | -3.5961 | -54.673901 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb1736f-1f35-3483-8dab-eea371650a51 | -3.0209 | -54.135601 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d78eecc1-e831-3a0c-af0b-86b975a75375 | -3.4831 | -50.083199 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e7e58dd-ee2b-3c30-badb-d83116869ee7 | -2.9905 | -54.047199 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81e3043a-f893-37fb-a9aa-0f7fc5e7abec | -3.737 | -54.659901 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e5a538b-9671-3353-bfd0-4a0b791a36b2 | -11.387 | -46.6782 | 2026-10-08 00:48:00 | METOP-C | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd38817c-5f36-3734-bd74-049578fc02cc | -12.3895 | -47.418499 | 2026-10-08 00:48:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fae083f3-e7e4-3f51-9a29-3f2d069b5a4e | -3.032 | -53.9123 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4192ab3a-ca3b-3989-b622-4b79461f1638 | -12.2031 | -48.433498 | 2026-10-08 00:48:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5142b69d-a429-36f9-8f78-1bd22bbf49fd | -7.1916 | -55.1334 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54bfef3f-ca87-3339-9329-f3697340aead | -1.209 | -49.258801 | 2026-10-08 00:48:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f38e772-8323-3f6b-86c5-664043a32ab9 | -11.8609 | -43.546398 | 2026-10-08 00:48:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d29bfe7-f496-39f3-8fcc-b65ccc08d9af | -3.0634 | -59.2789 | 2026-10-08 00:48:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 842c825b-3971-3990-9c58-b959cb3b7485 | -3.0158 | -54.248699 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dfd3202-a65c-39da-8cfa-b688422854b8 | -3.0181 | -54.168201 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbdda346-720f-3458-82a3-55aa18765318 | -3.1663 | -54.095402 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 141d2c64-f485-3c88-a432-57ef2b57ea90 | -3.0256 | -54.110699 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab468fc3-0137-38db-aafb-a0057b51623a | -2.9841 | -54.0644 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bee36c85-8779-323a-828e-717d764c3f1c | -2.979 | -54.041801 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 338d0f53-28c6-31de-8b6d-5b19af3b41f0 | -2.9489 | -54.135601 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e7a6d8c-8b69-3583-b43b-6a51a770acea | -7.465 | -47.605598 | 2026-10-08 00:48:00 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6998e3ff-c052-335b-a8eb-ebefeee5cac6 | -7.2086 | -45.371601 | 2026-10-08 00:48:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2537076b-829f-34dc-ae80-3171329a7b8e | -3.0273 | -54.118198 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7e68ee6-f16f-3b38-8b1b-a1e051d5c2a9 | -2.0394 | -56.1992 | 2026-10-08 00:48:00 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49500568-4a57-31d6-8d4f-536351f70f34 | -1.7152 | -55.453602 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16dd5efb-eb08-3f65-9e2c-4d57f73df718 | -7.3828 | -47.607399 | 2026-10-08 00:48:00 | METOP-C | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f283545-f36d-3506-9afc-dae1bb17f54e | -4.5675 | -54.967701 | 2026-10-08 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 921efb11-22ba-3bc7-ac95-6be52cba93d5 | -3.5784 | -54.686298 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4e4a90f-cc5c-3f5d-925e-c3bb3e064145 | -10.9851 | -45.398499 | 2026-10-08 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30785e49-8385-3da0-9058-d1fd113b0554 | -3.1713 | -54.615898 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 809fb8f7-d17e-3b34-b2c7-bfc99ede58b7 | -2.4919 | -56.1091 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86e479e3-092b-3ed6-8499-1a6e095390bc | -2.9915 | -54.142101 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12f31792-a68c-3a72-80cb-a111ab09da99 | -2.4842 | -56.120602 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d08135a-c98b-36d7-aac5-1fe36861e0b6 | -16.9041 | -40.882401 | 2026-10-08 00:48:00 | METOP-C | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b2953d0-5701-3da5-92e9-c400241f0850 | -6.3224 | -55.331402 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24974f7b-0062-38cb-b34e-4cab6ffa93c8 | -3.6542 | -54.294201 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1e00c06-6bbf-3b76-973a-6221839af6f5 | -3.0913 | -53.720699 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53b687c0-629c-3361-8467-2e4f97fc29e9 | -3.2736 | -54.023998 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6116c14-cb40-3036-8698-fc6bcfed7ac4 | -2.5164 | -56.262199 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5875dc14-9353-3f71-9428-63589adb9abb | -2.9564 | -54.213799 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 936a179f-8f78-3698-b5aa-7ea021361ac2 | -7.2188 | -55.117599 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a479f1d4-5ee8-351c-a518-d2829aacb03b | -2.7863 | -54.1003 | 2026-10-08 00:48:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 954835d7-809e-3379-a221-9dcf09be944b | -5.8361 | -52.063702 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0b1d140-773b-30fc-ad3a-4fc7f225e27b | -6.4791 | -55.297501 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cac15681-439a-39f8-ab1e-0314443e8602 | -2.8849 | -54.125999 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c49171d-0675-3304-a1a9-56b8f527070e | -2.8244 | -54.131401 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6579e645-bcf9-3fd4-8893-6aaac295c518 | -3.0683 | -54.253201 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bc34a4e-9533-3cae-9fad-5d4c3db74231 | -6.0995 | -55.714802 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39ef1458-4226-371d-a9e8-3ea152685b4e | -6.2352 | -52.870098 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57b7ed19-be94-36a0-8c70-03b7f5090b67 | -3.5166 | -54.640598 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf17979-5a8e-375a-9c1b-2685ef21305b | -4.3554 | -43.798801 | 2026-10-08 00:48:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 883d31ee-2cc2-3c98-952a-f9d116f0fa50 | 2.4373 | -50.833599 | 2026-10-08 00:48:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9355c1b4-d7b0-3870-a26e-bc83310fdcf0 | -6.1464 | -47.9226 | 2026-10-08 00:48:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68c3f56f-79ea-3602-8f57-73fd02a8adf0 | -7.2317 | -44.282501 | 2026-10-08 00:48:00 | METOP-C | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6521f687-4717-30a6-ad5f-4bd9fb9215e8 | -3.598 | -54.681999 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29e12f07-2071-3a4e-b7c0-c7912489150d | -3.0008 | -54.0924 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bb68555-1e52-3aa9-9471-2c542c93eca0 | 1.3339 | -50.837101 | 2026-10-08 00:48:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 937af680-6d20-338c-9c19-21712354dda6 | -1.798 | -57.124802 | 2026-10-08 00:48:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68e56849-7537-3ae0-9f88-83e328652c63 | -9.0257 | -49.198898 | 2026-10-08 00:48:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23760976-0c88-34b1-a627-5dc1f82917fc | -11.3522 | -51.8741 | 2026-10-08 00:48:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f71f9ec-e60b-3ead-ae32-c323164624bb | -19.997499 | -49.096699 | 2026-10-08 00:48:00 | METOP-C | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3f5eda1f-5c80-3ee2-a47b-8c3b4ded8d10 | -3.5808 | -54.651901 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9769923-af90-39e2-ab52-f0e0d226a999 | -6.0999 | -53.5033 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75d845af-ff7b-33a0-9388-133a151ed4c1 | -8.0805 | -55.308899 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d005b50-5c66-3c76-9352-26105d09a3a6 | -1.4584 | -54.780602 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb5c5656-36bc-31c8-af63-6b694f5ab47b | -2.9529 | -54.198601 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bb1942a-4e27-390b-9ef6-d2935db7ab80 | -3.7272 | -54.661999 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3f973ed-6298-3ac5-924f-b1508c9afbe3 | -6.3336 | -43.353802 | 2026-10-08 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb52505b-d536-3696-af7d-042896a4b864 | -3.2697 | -54.686699 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb699b46-3592-3b41-a7b8-e419ad238aa8 | -2.931 | -54.147499 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 799537ef-7a78-3f84-9182-4f2f19a0020e | -2.874 | -54.893101 | 2026-10-08 00:48:00 | METOP-C | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f608156-0f38-356a-bb09-c0d80a6a2eda | -3.0134 | -54.1931 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8454f203-4650-3dc2-ad5b-3ff0da396b79 | -3.5747 | -54.670101 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f972e2ef-8d3d-355c-9e0c-62ece54cd929 | -4.9433 | -49.218498 | 2026-10-08 00:48:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 412a24bd-13c6-3395-ae63-c51496056542 | -3.029 | -53.944302 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82a02e5a-47d2-31b5-9559-16841a37ff0e | -2.5031 | -56.067501 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5813a45-93f5-34ae-ad2d-dbd3028cc603 | -2.4744 | -56.122799 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f868e67d-6e12-3aea-8ff3-4ee36458cdbc | -10.2456 | -49.656601 | 2026-10-08 00:48:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c11fcba-2d4f-3bad-ae59-fb8f2fd21a7d | -6.5023 | -55.4025 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2ad9366-fb89-3bee-9e9d-91d76bf8b91b | -6.2564 | -52.8731 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85549de5-e7ad-3be0-86eb-14a7d6fcaa11 | -14.9212 | -48.089699 | 2026-10-08 00:48:00 | METOP-C | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b4b5b45c-d2ba-332c-9c32-c6df3ec3b938 | -3.054 | -51.217899 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a610449-b45e-311d-b692-73da405239df | -5.8722 | -53.497398 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8f55603-2582-3578-845d-6318c5fc1540 | -3.0106 | -53.909199 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README33.md)
