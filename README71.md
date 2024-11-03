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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 504b49bc-07dc-3f30-891e-05655108eec3 | -2.4079 | -53.96764 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ade3f185-b039-3cd0-93db-2186fd31d85e | -2.40457 | -53.94329 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2f11b3c-8c75-3cd8-b344-6119442e37a3 | -2.40441 | -53.96709 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed7fea7b-dd37-3391-aa81-2c7236466b41 | -2.40107 | -53.94273 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18566716-e99a-31cf-ad5b-991d90c1f661 | -2.38402 | -53.95996 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97466d61-21be-3d70-b423-5fa132a0a859 | -2.38342 | -53.96382 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8242bf84-64a2-3129-a47c-8eddd1c814a4 | -2.38282 | -53.96767 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3b968c9-4ed3-35d5-ad4b-e752169ce1aa | -2.38221 | -53.97151 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc16d58f-3642-3406-9f3f-fa815d0f2cd2 | -2.37992 | -53.96327 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 479a88b9-c289-3d9e-8c25-4160cbcd9a01 | -2.37932 | -53.96713 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c74ab44-a7d3-33fb-a05d-6e0b318476eb | -2.37232 | -53.96605 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6692dee6-6262-328d-b663-e5098017abb2 | -2.36822 | -53.96936 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 389c2731-1eea-3b7d-84a5-4065d423fac5 | -2.34392 | -54.07943 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37ee7b77-f52e-3920-8519-cf0cd7a2ce8e | -2.31341 | -53.97658 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cb09513-ee79-3837-bab8-6f78b5a5c760 | -2.30991 | -53.97604 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ae052dd-17a1-3bd3-a89a-e7b564f66cd3 | -2.30425 | -53.94065 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43bd9d2b-6838-32df-8c42-c5c190999de0 | -2.30075 | -53.94011 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d2766fa-5c23-365a-91df-54a3b0ea747c | -2.29906 | -54.01877 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c7f5528-47bb-3e60-bd25-0d2d2ae5ac56 | -2.29725 | -53.93956 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06f33477-cea3-3d67-9630-245e3b401769 | -2.29642 | -54.0174 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae58b75b-6641-312b-908b-1f255f2120c0 | -2.29583 | -54.02124 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5238eaf9-08e1-394a-a0e1-33ac155f388b | -2.29558 | -54.01822 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8637e757-8935-3d15-a35d-6427a6da3f33 | -2.29514 | -53.99837 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e10c3e5e-7d91-3f89-af7c-cf97666aa11b | -2.60781 | -54.51546 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d897fc9-0042-397a-bd33-d821af467f31 | -2.58219 | -54.38552 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 3d7e3e99-0746-3407-be0a-3160a19c97f9 | -2.58162 | -54.38926 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 1f891be4-c34d-34b8-bcbb-9091e1f09661 | -2.58104 | -54.393 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| c14fe6b6-858e-3558-bfc5-0dbcb18037c4 | -2.57874 | -54.38499 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 31e763b4-a491-3d7c-9d24-2056e1774c04 | -2.57817 | -54.38873 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b7c7e0bc-b9a0-3713-9213-63dc0fc8df4a | -2.57759 | -54.39247 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 221171bc-3e7b-3855-9832-390d0877977c | -2.5753 | -54.38445 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 648a7ee1-249f-30ef-a781-2d616bc4a63e | -2.57472 | -54.38819 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a8aabb33-3630-3f0a-b549-ab328c07c216 | -2.57415 | -54.39193 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dd112d9a-804e-35a4-8ff3-3f7aff372aaa | -2.57127 | -54.38766 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 65fd278b-b1c3-322c-9c18-08bb8a0d35db | -2.48559 | -54.30923 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c577dcb3-5743-344f-8a1d-bd05af2ef924 | -2.48214 | -54.30868 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e66fef29-a5be-3454-8f9a-0750b57adbd7 | -2.46851 | -54.22641 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 759dd84e-dafb-38df-92da-16b865985576 | -2.46505 | -54.22583 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3528ffd-b284-30c7-885a-7d4bbafbdd58 | -2.45902 | -54.70679 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| eac6617e-0592-3cef-a027-3c866ef398c8 | -2.30181 | -54.50692 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91af7d75-4956-3fee-b0a5-759c7f2a7992 | -2.25729 | -54.47741 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c9aac6d-d1ff-35ed-a411-81cc65d319dd | -2.20782 | -54.23772 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4e974038-bc9c-389b-9039-7b615b4c1d1b | -2.20436 | -54.23719 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3172709b-198c-3a4f-84e8-777062cb34b2 | -3.93672 | -54.17781 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99a2456b-931c-35fc-8594-fc655cdeb142 | -3.85117 | -54.30861 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b400195-241b-36cd-bee7-fda6bfc8ffbb | -3.84684 | -54.76093 | 2024-11-03 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1d92b8a-c306-3b4f-b343-9703ecde005a | -3.84627 | -54.76463 | 2024-11-03 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b650b847-5677-3f71-85cc-d54a43eb55a3 | -3.83939 | -54.78639 | 2024-11-03 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f27465fe-e49d-3cdd-bdd2-647f548b7d2a | -3.83596 | -54.78585 | 2024-11-03 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e94bc4c-6eeb-3319-940f-425a0402778e | -3.76175 | -54.51799 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea136c01-25fa-3df0-b0b1-d308871adf9d | -3.75309 | -55.34319 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f64131ae-c3e5-3e54-9ba7-cf47bcf12c1b | -3.70705 | -54.10067 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e22ca736-e9c4-3daf-87ff-8c17110da1d3 | -3.98382 | -55.11638 | 2024-11-03 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ad8f3e2-1a6c-30b0-b643-847d0b36115c | -3.98098 | -55.11223 | 2024-11-03 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1766f40-3adf-35e9-84c3-a1f90c60580b | -3.91352 | -54.30541 | 2024-11-03 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8a8d592-abb5-3e78-a278-bad14588c1bf | -3.89064 | -54.05505 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deb64135-3fa4-3733-9095-15015a23fe87 | -3.8434 | -54.76041 | 2024-11-03 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddec15f3-bdf7-3b38-ab7c-deb9d0c7e72c | -3.83996 | -54.78267 | 2024-11-03 05:08:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d325082-70a8-3f3e-8552-fac6cb7e847e | -3.79075 | -55.30128 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f079672e-f99a-3939-9585-e40bd905a478 | -3.78737 | -55.30075 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 296fc83a-df40-372d-a378-abe7621a97ae | -3.72272 | -55.33846 | 2024-11-03 05:08:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c9f21cf-807c-37de-a319-97398e5b85db | -3.71057 | -54.10121 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32608476-750f-36ca-be87-7394cef26cc0 | -1.87807 | -56.32033 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8d2d06d-bbaa-3fb9-9c89-da3fa45d6617 | -1.87752 | -56.32378 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f1b5e82-d4fa-3fe7-9038-9c4c689bd43a | -1.87475 | -56.31981 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77da2f3b-87f6-3b4c-8618-d92861be8918 | -1.8704 | -56.0257 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7696e209-8335-3f70-a11b-1211f36366d4 | -1.75186 | -55.42562 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e72a6d2c-8349-33cc-811d-50e25d9c0121 | -1.74907 | -55.42163 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b44ea0ff-05f3-3e8b-a885-be50255f8a89 | -1.67115 | -56.23826 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4676ef71-cb56-312f-9487-4a185fa2eabf | -1.6421 | -55.2405 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e64acee0-4076-3ca5-8906-5601b63c1054 | -1.61923 | -55.23336 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff6dcdd3-2069-3718-8e8e-33ce130b6d3d | -1.58455 | -55.192 | 2024-11-03 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae4fb176-7058-3ed7-8bb9-6766129b5093 | -1.58347 | -55.09818 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9d3eb86-52dd-33e5-b634-69183024999a | -1.58235 | -55.10524 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f22ca75-227a-3213-ad84-bf52a18030b8 | -1.58159 | -56.16081 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ae6f36f-3fd6-369b-bb55-0f3b3c9996b5 | -1.5812 | -55.19147 | 2024-11-03 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b53d57c-cff5-31f3-9b16-0731da7bb6a3 | -1.58068 | -55.63078 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9da55f7-f109-3fad-836a-e9f4e6bb35b9 | -1.56451 | -55.15298 | 2024-11-03 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f573d9ac-786e-3f83-aec1-1dd17c0e90da | -1.56116 | -55.15246 | 2024-11-03 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af2dff6a-0401-3058-b520-964fa991ca4e | -1.55763 | -55.00006 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab5d88de-283e-3070-9b4b-6af022d15c75 | -1.55427 | -54.99955 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b75ad4ae-4a87-3529-b688-d4596aca79ac | -1.5444 | -55.73148 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b793018e-aa61-366c-8cc3-5ea43a761827 | -1.54162 | -55.7275 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f4c0007-3227-3e1c-ad6b-db0e6767c49a | -1.53196 | -55.05408 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db6e2c4c-2ca0-30e5-ae79-d4ec08e890d7 | -1.47683 | -55.14306 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ad21cc6-366d-3939-aae1-9871c9cbf93d | -1.46853 | -55.16303 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c64ed3a-a444-39c3-a66b-954c1206e451 | -1.44035 | -55.42051 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4c60b73-c3e2-38b2-9455-1a7d5eb88aea | -1.3902 | -55.84893 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fac390df-b8aa-31fd-be26-bc3c5b1959cb | -1.38688 | -55.84841 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c316623-341c-376b-95ca-3ccfbd6d26ff | -1.38634 | -55.85186 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fb8affc-abc4-3480-b76c-6e57905b90f0 | -1.38302 | -55.85135 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4d81e67-db5f-3db0-90e8-0beaaeb3b254 | -1.37313 | -55.37759 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0406e974-1d48-339d-ae5f-0874951d66d9 | -1.37111 | -55.45567 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23b931cc-0abc-3c5b-bdc5-12ee2a629aaf | -1.36088 | -55.36858 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 273e172e-4850-30e0-8043-5e83aebb2b4a | -1.35754 | -55.36806 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4fd8ce4-4ac2-3bd5-b694-f2fcd59b15b8 | -1.357 | -55.37154 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ea9dc8a-f735-3b15-9599-6a072ace83ec | -1.3502 | -55.32764 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4899365e-8dc0-39a5-84ff-3a15d8833882 | -1.32727 | -55.82102 | 2024-11-03 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a391663-6f79-38eb-ba3d-3d2a6788b62b | -1.31085 | -55.23569 | 2024-11-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3816df04-3b38-3d0d-a12b-2716bb8a1723 | -1.3024 | -55.46289 | 2024-11-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README72.md)
