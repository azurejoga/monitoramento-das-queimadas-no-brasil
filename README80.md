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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11180a60-c3ed-3c3a-a0f4-5139de5fdd5c | -6.66708 | -50.90306 | 2026-09-18 05:16:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 074d3279-cb7a-36fe-b5e7-9ae80edca826 | -5.86491 | -51.94737 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3328c56-319a-39aa-9101-febf09851b05 | -4.48719 | -54.97813 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c6d4560-5c32-36cb-b5ac-2baebf78f3e0 | -2.90032 | -54.18148 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22600429-3fd8-31e5-9983-28b3ee72bc62 | -3.69915 | -60.62893 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bf58abc-48a1-32e2-8ead-e0a79e4e5668 | -4.42742 | -55.5205 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10ccedc5-98fd-3dde-89ed-d301026542e7 | -4.71169 | -55.75637 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59de207a-1f03-3274-a3e7-fbcfff9f6d85 | -6.36625 | -58.28891 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdcebcf4-681f-3234-835b-32d710d1499f | -3.48007 | -54.71524 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d89fc95b-b1a5-3a38-a932-3891914cb4f0 | -4.48726 | -55.49281 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60a8bc33-aa35-3e81-ab59-8483cc04ca04 | -2.95965 | -57.70537 | 2026-09-18 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 151be00e-7b4f-35c6-a4b5-fec92545e220 | -5.9756 | -55.3567 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d58b2de9-a4fc-3a9c-81ed-76fbab8ade71 | -4.49991 | -54.85147 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9177b34f-0ad8-3af7-b69e-7d932a0a4e51 | -7.6736 | -46.10908 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b07d2ec-745e-3e87-ad30-e828674e0763 | -5.75213 | -51.92297 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d671cc5-b95d-3f15-9eb0-274f7ab3ae69 | -1.16032 | -47.63146 | 2026-09-18 05:16:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a5cbe0a-6c74-35de-ae9c-8125819df853 | -6.46338 | -48.0058 | 2026-09-18 05:16:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6adbea5d-6707-32f0-aacf-0a94535e2e69 | -8.53566 | -44.5528 | 2026-09-18 05:16:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4747bcd2-aa39-35e5-b58c-d71b00fcaa8d | -5.86605 | -52.05488 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae4d49ac-a086-346b-9da3-e2fbae9aff6b | -3.33547 | -57.86152 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12497045-6105-31c6-8518-09170fd427e0 | -3.6447 | -58.55994 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d66e473f-f0e4-3d71-affe-a2c8df71d18d | -3.40076 | -57.23824 | 2026-09-18 05:16:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ca45984-8498-324e-b63d-86ca16a371a5 | -2.83062 | -48.65492 | 2026-09-18 05:16:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e17eb741-15e5-3306-9fea-fef1a271493f | -7.68192 | -46.09485 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a72ba514-6ba7-30d5-830c-7bf0d94ee969 | -2.82615 | -50.48174 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 545c4e07-8103-37c4-b00b-c3d64edacbb0 | -4.16715 | -54.4101 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0352550-9717-3232-ae97-bd3b80c018c0 | -3.44057 | -58.20711 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3b4c82e-bb82-39a0-8ad0-9baa3b14c77b | -2.80637 | -57.62002 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b72c10d-92f1-314c-bbf6-8b00192d0cf1 | -4.51339 | -56.08631 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0981ceeb-a9a7-3e3d-be44-f6b5a1f62142 | -3.13108 | -59.02602 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c94464f6-631f-347e-b880-4f1c5ca3bf0d | -2.90795 | -54.17866 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5721e4c-f97e-3f2e-9c3f-6bcaf0286c0c | -4.50682 | -54.96571 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 316ea8cd-7cc4-3b70-8213-dc8f7e84916d | -3.48065 | -54.71146 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 636ec318-d08b-3ab1-b8b1-e8e1ef78d77d | -3.44899 | -58.19749 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d10f5755-3c46-3982-84f2-9fab409efa44 | -2.91147 | -54.17921 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08ba6aef-f177-3df7-ab6d-c287c9abbdfd | -4.275 | -55.54956 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34cdf271-9621-3781-aa63-ee7a41c45d7f | -7.79466 | -44.90143 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dacd360b-f80b-3242-907d-41af72632bd0 | -7.39107 | -44.50124 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61ca8879-8d40-3424-8f96-c87fcac5d95b | -5.88944 | -49.77809 | 2026-09-18 05:16:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b371afe-0a29-3f89-ae1c-6638a8a9849e | -3.76103 | -51.13722 | 2026-09-18 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfe8da09-28b3-3149-afd8-3af128a0a5de | -5.17776 | -56.18201 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d18110a4-b528-36d7-a586-d79c33c9c746 | -3.36646 | -50.45132 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7c357c2f-def2-3293-b05a-ca5f9b925ff2 | -3.27944 | -57.91722 | 2026-09-18 05:16:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0a733de-0a1b-3f83-84af-71c30fc5cd18 | -3.81133 | -58.89712 | 2026-09-18 05:16:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9345797-d806-38bd-9d4d-d1479fcf3f61 | -6.52285 | -49.89115 | 2026-09-18 05:16:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| af8c6c46-cec5-3d0b-867c-f9cff366d692 | -4.55019 | -54.92917 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04a23bee-a291-3588-8eb6-b486e4e31c08 | -7.66225 | -46.09755 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 84f19b1e-6659-3d6c-b2fd-e747a5f15dae | -6.67031 | -50.91279 | 2026-09-18 05:16:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfaf4a2e-cc1f-3517-aa65-ce962c050b8c | -4.50969 | -54.96995 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abfc2a15-6e1f-3945-a2ea-4f3c9d639ab2 | -3.91805 | -55.74755 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bf3bea3-7253-358a-86ef-54f9771942b0 | -2.74812 | -57.62521 | 2026-09-18 05:16:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 482016c5-6a56-3be9-b598-bef08a78f91a | -3.9664 | -56.13034 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 553918e0-8f05-3c0e-ae3e-64920c369ded | -2.89806 | -54.17002 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cf496e1-c89e-3a11-9582-642f3fd7505b | -2.81966 | -49.24135 | 2026-09-18 05:16:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31e688d1-02c6-30aa-b1a0-54afe0cc1598 | -2.82803 | -50.46915 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 50acface-1dbe-3066-bda7-a84cf3679299 | -2.6085 | -54.75728 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b6297ad-ab9c-3208-baa0-2307aadd22a4 | -3.37466 | -50.45126 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2dd038d-e5db-33c7-9d41-0e694918bf74 | -3.03824 | -51.37151 | 2026-09-18 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f1385380-af9f-3219-85b2-18013d4b0852 | -6.02771 | -51.80811 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd6c0088-3604-3e1d-ba8c-278f7e308248 | -3.46682 | -54.70935 | 2026-09-18 05:16:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 902b0598-bf43-3723-aa51-e1a1eebd1849 | -3.31713 | -57.84784 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a1b1058-62f7-3473-80e9-8a32601dc627 | -1.49233 | -54.97181 | 2026-09-18 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d96a3be0-4534-3b2f-96ce-8f576ee38e2c | -3.55438 | -58.55298 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50dc6025-996a-3e37-a4d3-52fd012358ac | -3.69703 | -54.54486 | 2026-09-18 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6694f00d-2421-36b5-add9-06051f8d3990 | -7.79541 | -44.90958 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d845ee39-a8f6-3544-b7bf-a5666b860d60 | -7.80224 | -44.89652 | 2026-09-18 05:16:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 92702bad-1220-3b6a-8e8f-565e87c800c6 | -2.05542 | -52.16455 | 2026-09-18 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 709bdadf-f9b8-3183-b7ac-714054db8b75 | -3.02672 | -51.33529 | 2026-09-18 05:16:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6114f5b4-6ba4-3938-8482-0cfd75a47a2e | -5.85637 | -52.03459 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fe4c64f-fd46-38a1-99c8-e1eca263556b | -2.77775 | -57.20318 | 2026-09-18 05:16:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6629aae8-7c02-3d98-ba51-73340f13882d | -4.88123 | -56.05958 | 2026-09-18 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae3546ea-2238-3c84-90b1-22f7fcc0cff7 | -5.75569 | -51.92766 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30e01be8-a98e-3b52-89bd-db0b8cbdbd75 | -3.44393 | -58.20765 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6ea5653-59ab-3925-b54e-b54d1e743013 | -7.57163 | -46.35368 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 775c66e9-6eec-34f7-9d23-1fec7a3c4891 | -6.60789 | -44.20376 | 2026-09-18 05:16:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ee9d8ba-1e44-3340-8234-02d4f8c3235b | -4.51116 | -56.07874 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbf55d15-d5c1-3da8-bc62-cac329984403 | -4.43024 | -55.52468 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1abae693-16be-3a9b-b3ff-77c6bc605454 | -3.92363 | -55.75577 | 2026-09-18 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a352de61-4c2b-36aa-8c73-caa17a124fee | -3.69597 | -60.6013 | 2026-09-18 05:16:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a9e3391-3236-365b-9734-2bd55a68460a | -1.78426 | -47.83386 | 2026-09-18 05:16:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59732a96-a759-38d1-a010-56a8058d42c7 | -6.10095 | -57.62767 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6190641e-aad6-396b-99b2-bd7b4cd06f9d | -6.15754 | -55.70061 | 2026-09-18 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40878aa1-f1bf-32bf-a595-7dd4ed0a20b3 | -2.90034 | -54.17839 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a2e22f1-b197-3223-91fe-b75dc5371417 | -5.73881 | -52.2416 | 2026-09-18 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed7d326f-2dbc-3ec9-9bf6-e94ad302042c | -4.3717 | -55.42653 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a1ac297-6857-3ea2-8ede-58aef4f3ccf3 | -7.4579 | -46.83931 | 2026-09-18 05:16:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e962f07-5c72-36af-87c7-059c4a7bf5e2 | -6.62252 | -57.9806 | 2026-09-18 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54e4a30f-f3f4-3afa-ae7f-ae4dbbe5f1fc | -2.81842 | -50.47365 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 9fb9856d-767e-3a00-96b2-bc5901bac68c | -2.8962 | -54.18486 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 20440571-5222-3dca-93ea-3f21a20b2d29 | -3.33576 | -54.17196 | 2026-09-18 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbcc61a9-ca0c-35cf-aab3-334610b2e460 | -7.66157 | -46.10272 | 2026-09-18 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51649c77-df91-325d-a133-11d688c77626 | -4.42797 | -55.51692 | 2026-09-18 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd94f852-c062-3764-b24c-a887d1996df3 | -3.14527 | -58.65402 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b063ee3-6e8d-34c8-86d5-ce3ad6fe7607 | -4.57393 | -54.91314 | 2026-09-18 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2fe73ef-0aa5-34d0-a290-7bdcf7da74af | -3.34135 | -59.44817 | 2026-09-18 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5beadf15-27e0-3b2e-b543-cefb1fbd26cd | -3.43608 | -58.2137 | 2026-09-18 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67c10238-7da3-3c1e-996e-8bbacc01b68c | -6.37235 | -58.29347 | 2026-09-18 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce497705-9333-3c16-8dae-07b83708509f | -2.25722 | -52.0265 | 2026-09-18 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c536c72a-64bd-3ca0-a683-5c35fcf8ef6c | -2.82347 | -50.47013 | 2026-09-18 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 6f604cef-7f80-37d3-bfc4-2718b362831c | -2.35854 | -55.23315 | 2026-09-18 05:16:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README81.md)
