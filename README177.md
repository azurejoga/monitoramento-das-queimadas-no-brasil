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

## Dados Diários - Página 177

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2078a68a-9767-3e1d-92ff-b41e9173bdee | -3.37 | -42.31 | 2024-10-04 05:05:09 | MSG-03 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 8e27430c-4d71-3e4a-941d-8332e9aaf16b | -3.37 | -42.27 | 2024-10-04 05:05:09 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18d253bb-1dec-3be0-a65f-ac66263434b0 | -3.29 | -50.49 | 2024-10-04 05:05:09 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a622798a-1099-3f0a-821c-f46c9bcbeb49 | -3.29 | -50.43 | 2024-10-04 05:05:09 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 455db30c-9788-3e4c-9816-b826c5eac2c5 | 2.69025 | -61.31839 | 2024-10-04 05:46:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c4a8a19-8794-3061-a563-5166b2fc5fbf | 2.68659 | -61.31902 | 2024-10-04 05:46:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f7d29e8-8a09-3c20-9281-522a4d3d7556 | 2.6859 | -61.31468 | 2024-10-04 05:46:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fa0c03e-8a90-3a8b-afe6-02c7f9964d2e | 2.59889 | -61.28662 | 2024-10-04 05:46:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4355b75-59ea-3440-9a75-41b518180951 | -2.95255 | -52.77985 | 2024-10-04 05:48:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4c67e7ab-ea30-38cc-b4c3-7aede00d7c0f | -2.95152 | -52.78685 | 2024-10-04 05:48:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 44297967-7ab1-3243-a5df-ae30ddc5626f | -1.75871 | -54.44932 | 2024-10-04 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a79447c6-24af-3c27-80f8-9cc93119871e | -1.75254 | -54.44835 | 2024-10-04 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 217c26a5-cd2d-3863-8440-3713068b09e1 | -2.97954 | -53.72991 | 2024-10-04 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78468dd6-967c-3b87-87d5-ebefa2300bcb | -2.97841 | -53.7294 | 2024-10-04 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 390c8cb2-ecae-3d8d-93c1-5041901cfa21 | -2.97383 | -53.72332 | 2024-10-04 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15c4f04f-51c3-36fb-ac46-b55a6da7d2fa | -2.97298 | -53.72892 | 2024-10-04 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b9b68087-aedc-3e98-ba61-8808195d9acb | -2.97265 | -53.72278 | 2024-10-04 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1b8e1e2-14ef-3f49-a769-9cacbd1a0227 | -2.97184 | -53.7284 | 2024-10-04 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecfa3ee0-a9bd-3ab1-8263-61f49bc36954 | -2.94927 | -53.70797 | 2024-10-04 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e0d3a98-be0d-30ce-a1d0-b0234df47425 | -2.20177 | -56.71597 | 2024-10-04 05:48:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 300532e0-2add-380a-b7df-a8e8250f5c7f | -2.20125 | -56.71934 | 2024-10-04 05:48:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77232bf2-9bf2-3bae-b664-1ab3e9f91695 | -2.19937 | -56.71774 | 2024-10-04 05:48:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bee0ee94-8968-396a-b449-35c30b03401e | -10.69047 | -69.0293 | 2024-10-04 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e3136e5-82cb-37ef-b2d1-1814f8a78b47 | -10.68989 | -69.03288 | 2024-10-04 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40810784-1802-32e0-8ef2-caacfdb32d78 | -10.66407 | -69.06541 | 2024-10-04 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2c9f2dc-cb4f-36bb-bb50-9129915ef985 | -10.64559 | -68.7364 | 2024-10-04 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fd22da9-5ceb-3475-bd07-d0b6d2fc63e1 | -10.50956 | -68.67084 | 2024-10-04 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27957910-9271-3104-9c94-ae273f0016c5 | -10.509 | -68.67438 | 2024-10-04 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d9f9dc4-f3ab-3359-82ad-de6527b01d71 | -7.70533 | -55.2059 | 2024-10-04 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38263b99-1f8a-3dd4-ada5-c3bd67a6ed4f | -12.60976 | -56.48534 | 2024-10-04 05:50:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a052bf2-ee85-30b1-985e-18f42896d4cb | -12.60919 | -56.49037 | 2024-10-04 05:50:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b57bb07-3547-3dce-b5ae-1a0863c28243 | -6.89749 | -59.05223 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08edb66c-0f23-3c93-ad80-487f370ca81f | -6.87722 | -59.03774 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 330757d9-8b3b-3175-9cb8-b3f0e79ecdac | -6.87645 | -59.04319 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 31f8cd0f-f464-3466-8d78-1b5756c97fd1 | -6.87307 | -59.03159 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57e02ee1-bf0e-3137-b3a4-1e634b18d770 | -6.87231 | -59.03699 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9b8ae32-3b03-3fb4-bf4f-d12676ff912d | -6.97619 | -59.09784 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ee9f70dd-dd80-361c-ab58-7e61e1e90e05 | -11.76951 | -58.88947 | 2024-10-04 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e3072559-6cd3-35bc-b27a-20b3689516fe | -11.76544 | -58.88835 | 2024-10-04 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f03dea13-dd71-34d2-ac33-3177ad8f9a4c | -11.765 | -58.89174 | 2024-10-04 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b543dcc-b72b-30cc-8cae-2dccf62a109a | -11.76419 | -58.88873 | 2024-10-04 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d730d2d6-10fc-3088-a80c-5a443bbd7265 | -7.14044 | -59.31909 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae7bc875-3334-3010-982f-95c0218ff618 | -7.13634 | -59.31312 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 684eb075-7a1b-370c-bed4-962cd5bc0d18 | -7.13561 | -59.31835 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f7ae11d3-6b81-32f4-8a2b-2887ff55e2fa | -7.05555 | -59.29885 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79bf4f53-cd14-3b52-9e7f-f38be6253644 | -7.05479 | -59.3042 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcd8b7f6-fd59-363f-b075-38dbdaa34469 | -7.04997 | -59.30347 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf6522dc-f4fc-336a-a6fc-8b808edf6821 | -6.71676 | -59.1298 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5606709d-4ff6-314f-83ac-ac3a410f1128 | -6.71188 | -59.12917 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf53e886-95dd-3a27-9ac1-60f46d7fa5dc | -6.71751 | -59.12436 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7bdee051-73ef-3cf2-84b2-0b3074db6443 | -6.71114 | -59.13453 | 2024-10-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7a189e39-2972-35bd-a0b2-3db6a5dec403 | -9.39248 | -61.04213 | 2024-10-04 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfbcc8e3-a8f5-3669-bd5c-e5b397d9fb16 | -9.39187 | -61.04652 | 2024-10-04 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fa6c2c2-df91-3d03-a910-75c49067f289 | -12.34584 | -60.72036 | 2024-10-04 05:50:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87a97ea2-965d-340a-a9d6-232bdc9d053e | -9.09218 | -61.13564 | 2024-10-04 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1995b50-eefa-365d-a7be-ae2dbb1585de | -9.09189 | -61.13392 | 2024-10-04 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 425f8599-d5ea-32d7-b1e5-2c30b947e2fc | -9.09128 | -61.1382 | 2024-10-04 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d780dbb-7843-3d8a-8cf9-578a13bdba92 | -8.8399 | -61.50288 | 2024-10-04 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 513a5f40-6817-3002-8a71-404d6a6a9d91 | -10.12335 | -62.76149 | 2024-10-04 05:50:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f36fac7e-7587-3831-a101-e2b11036562f | -11.02454 | -62.5919 | 2024-10-04 05:50:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4cd6db4-9d88-3dd2-a357-89f1f774e10a | -11.02045 | -62.59129 | 2024-10-04 05:50:00 | NOAA-21 | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb608075-88fa-3a7a-92d5-5bc2030380b1 | -8.75906 | -64.10395 | 2024-10-04 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6244ee88-7289-373c-9960-fb4b05aef7de | -8.75543 | -64.10341 | 2024-10-04 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95f518d8-16bf-3520-a16c-6a8e8a3af2ed | -9.53977 | -63.62174 | 2024-10-04 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74a29d4f-50cf-3a01-9f23-56bd65370ab4 | -9.53601 | -63.62116 | 2024-10-04 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae52bb4e-7490-35a4-932f-a0482340a207 | -9.752 | -65.51493 | 2024-10-04 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae979b92-ba2e-3bfd-9352-96ebecffa950 | -9.5989 | -65.66925 | 2024-10-04 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dc4425a-5efb-324a-907c-f59d07d5b979 | -10.5726 | -69.43738 | 2024-10-04 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17f787ff-f50c-3aad-a910-a5b9d9b1521d | -10.53937 | -69.33389 | 2024-10-04 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 222285e0-df33-3880-8855-46516ea4259c | -10.53878 | -69.33754 | 2024-10-04 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c08e9d4-238f-38c3-b6ef-f4e5c679bfb0 | -10.53719 | -69.32603 | 2024-10-04 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fa28ce8-d9e1-30dc-85cc-9cea526382b1 | -10.36947 | -69.25048 | 2024-10-04 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a73ab24-6cc0-3d0d-9ea5-cd8862e504d1 | -10.36889 | -69.25411 | 2024-10-04 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0fa37da-94c7-3ac0-89c5-e7ef851c66a7 | -10.36611 | -69.24993 | 2024-10-04 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0420fe6f-1f76-34b4-8183-a6fa4748dde8 | -10.17005 | -69.35999 | 2024-10-04 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b384c4db-8028-353e-97d2-cd3921e6e20b | -9.23921 | -71.90276 | 2024-10-04 05:50:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a43065a5-f914-3fa7-8991-9a9e31c771d4 | -8.22884 | -71.05706 | 2024-10-04 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b218eb22-3497-3948-bf6b-9647cc1559f5 | -7.83001 | -73.07524 | 2024-10-04 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec21be2d-7e22-36f8-92cc-02ec460fd641 | -7.8187 | -72.93961 | 2024-10-04 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cc5f8a4-61bd-3ce1-a7f8-0b39899b2271 | -7.81803 | -72.94348 | 2024-10-04 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc78290c-6581-3b79-a8b8-d20c9311d5a6 | -7.79611 | -73.06944 | 2024-10-04 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa673239-a9b4-3656-88c1-d123d3b3896e | -7.68546 | -73.05529 | 2024-10-04 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f6d11d4-5418-3176-96ca-43f02301932f | -7.63665 | -73.088 | 2024-10-04 05:50:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23e5581f-02d0-3c71-83a7-f7061aa61789 | -7.63597 | -73.092 | 2024-10-04 05:50:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c6057e6-966d-3ecf-bb1c-ebd630277652 | -7.45487 | -72.70081 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2219ae73-371e-3040-bd35-edf9055a66f9 | -7.43707 | -72.58115 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8916c42-4c7f-334e-a5c0-83de6ec9eccd | -7.43361 | -72.80005 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9607fbcc-c137-328a-b7be-6261e5ea7937 | -7.42881 | -72.72787 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 193c4184-652d-34e7-ac75-096356a44265 | -7.42815 | -72.7317 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33977925-2b40-36e9-9e21-0389bdee0d70 | -7.42399 | -72.731 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86b9fbdb-1277-3412-a2f0-bc94aa85b811 | -7.42333 | -72.73483 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1db0ea84-e95b-3998-89d8-60fbda90f1fc | -7.42124 | -72.8219 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3f9734d-78df-386f-b56d-6a018fe1a01c | -7.41982 | -72.73029 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7305b48-3b3c-30d0-9235-94d1fd129646 | -7.41916 | -72.73412 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f9f2eaca-1c66-3c39-a52e-6e9bedf64952 | -7.41705 | -72.8212 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b37aeea4-6b18-3442-b873-79409f520799 | -7.41286 | -72.82049 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f1643e1-cdcc-32b3-94f5-7596b4e442dc | -7.3924 | -72.50381 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f84c75c8-0fa0-3ea2-9c62-e79e7f08ca22 | -7.38253 | -72.79083 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fabdc79-5da5-31e3-8a7f-a81e33ed7b9d | -7.31111 | -72.755 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e55943ff-7716-3d93-b87e-8c7a8fede778 | -7.31044 | -72.75888 | 2024-10-04 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README178.md)
