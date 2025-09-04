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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf343de2-53bb-355a-a714-8df5805af758 | -8.0796 | -45.3617 | 2025-09-04 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 8b24728f-af3c-3f95-9675-62c251909f27 | -9.7105 | -48.9853 | 2025-09-04 13:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 2fb6ea0e-49c1-3f6b-96b5-27c2f0451768 | -8.9031 | -45.82 | 2025-09-04 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 3bd2c8c6-2e45-311c-bfbc-5ff1338ae889 | -4.9951 | -56.256 | 2025-09-04 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 161.4 |
| dc189b07-2251-3e70-be3c-55082ed772ca | -9.7108 | -48.9636 | 2025-09-04 13:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 5b7b71bc-b82e-37ad-9469-fec6f7db91ab | -6.2205 | -43.5558 | 2025-09-04 13:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 6c269009-1a38-3c73-893a-9e07f26ebd7b | -11.7385 | -47.7637 | 2025-09-04 13:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| be205f3a-e3d3-36fb-b498-2b1eb4a1f8ba | -4.9049 | -41.7696 | 2025-09-04 13:00:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 134.3 |
| e03fce33-1f48-3539-b614-e59c86fa82d5 | -5.6777 | -45.6089 | 2025-09-04 13:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| dd6fadda-0ddd-338d-8c1c-f1f0382be31c | -7.7036 | -48.7587 | 2025-09-04 13:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 115.9 |
| f11668da-3885-3d94-adff-af02b1cc3d43 | -12.4593 | -48.0885 | 2025-09-04 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f03b0d76-6d55-3523-90ed-08f2fa94cf93 | -13.8457 | -47.9764 | 2025-09-04 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 652f0991-8e88-37ab-8ee9-f19f25e89d7e | -5.6963 | -45.6076 | 2025-09-04 13:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 0245bd4a-4198-3b26-9502-8824f19427e8 | -9.3014 | -47.0986 | 2025-09-04 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 8eea6319-5e9a-3c1a-b6d1-3cf562d083c8 | -14.9865 | -50.0769 | 2025-09-04 13:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 6b7151be-9d8a-3af9-9680-938fce949d70 | -7.6851 | -48.7386 | 2025-09-04 13:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 291.1 |
| a1f9e922-7da0-342a-a8a6-c0c4b4bdc501 | -9.6919 | -48.9655 | 2025-09-04 13:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 5a0dbd8b-4a0f-36c0-82b2-87912ce83c46 | -6.2315 | -42.4515 | 2025-09-04 13:00:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 171.1 |
| 9a18fed0-7ae2-384d-b0cc-14aea3cd91f0 | -7.6351 | -44.7671 | 2025-09-04 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| b5a67118-f2fd-302f-adb2-0f541c29082b | -11.5779 | -52.115 | 2025-09-04 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 2fdfc239-0b08-322a-814c-820e6d5548ba | -17.0652 | -46.449 | 2025-09-04 13:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ffd92821-48e4-3a9e-ba1e-328d5ed31cf0 | -7.7252 | -50.3174 | 2025-09-04 13:00:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7d780999-8211-369b-92e2-fe82621186c8 | -7.6854 | -48.717 | 2025-09-04 13:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 8f0475dc-0b0b-3090-b7da-cd7ae02dfec6 | -11.5782 | -52.094 | 2025-09-04 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 0caa9101-3ac3-39a9-a136-dfe3ec15343b | -7.7036 | -48.7587 | 2025-09-04 13:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 5a2337aa-d753-3b2f-8383-9aac4d6620d5 | -8.8842 | -45.822 | 2025-09-04 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 91d563d6-0682-3dec-bbc6-fc60ff7d8c46 | -5.7 | -45.1786 | 2025-09-04 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 437.3 |
| 4e5cbed1-f39f-3287-86bc-47e5f64ddbfb | -6.2315 | -42.4515 | 2025-09-04 13:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 139.7 |
| 5f9c7d45-1660-33fd-9649-7187ab11fc4a | -8.3644 | -48.3116 | 2025-09-04 13:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ea322a81-01a3-3d1d-8d51-b3b5fb5903b8 | -6.2318 | -42.4278 | 2025-09-04 13:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| bc9798c9-6033-3f9a-beb5-b0a33fb9ec90 | -8.0799 | -45.339 | 2025-09-04 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 169.4 |
| e81049f1-b5cc-355c-a1cf-a58f19a8af19 | -11.7385 | -47.7637 | 2025-09-04 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| a756cdf4-e973-32ce-b649-cc911f1a8cbc | -4.9951 | -56.256 | 2025-09-04 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 173.2 |
| cb064f7f-01e2-398a-910d-2ee03b76c39c | -5.7002 | -45.156 | 2025-09-04 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 2bfbc9da-a870-34eb-b376-d4251760538a | -9.7108 | -48.9636 | 2025-09-04 13:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| ef1a3b25-07f7-3e95-a501-6d94be803a41 | -11.0062 | -45.9072 | 2025-09-04 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 32f6de0d-33bb-3543-b9ba-ef9d54360191 | -7.6851 | -48.7386 | 2025-09-04 13:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 174.4 |
| dae43346-e81b-345b-a9a3-c8983902f46e | -8.0796 | -45.3617 | 2025-09-04 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| ef045637-1fc2-3dd2-b06a-ddae500757d0 | -11.6599 | -54.5297 | 2025-09-04 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 9993bb2c-cb8c-3f73-97ee-87937069f1d3 | -13.8651 | -47.9734 | 2025-09-04 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 4da9f75b-8f50-34cf-a571-fe14473f7838 | -13.8457 | -47.9764 | 2025-09-04 13:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 91567676-1726-3c83-83d6-ebab71d94b66 | -7.0502 | -43.2724 | 2025-09-04 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| a235cbb7-2be6-3ac3-97d7-2dd0bef40183 | -6.1665 | -43.3273 | 2025-09-04 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| e9142d95-8736-34c6-833f-edd338454a29 | -12.4593 | -48.0885 | 2025-09-04 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 974eb07f-ad4c-3d7c-8f83-5d6ee773b3d1 | -7.7409 | -48.7772 | 2025-09-04 13:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 7a264821-e152-3b0f-90c0-8afb87d1432e | -6.2205 | -43.5558 | 2025-09-04 13:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 7487f5ac-e535-3223-b2f1-90fb0194c7da | -11.6335 | -52.214 | 2025-09-04 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 97ff2774-67f0-306c-8c3a-a880cc9dd631 | -5.6813 | -45.18 | 2025-09-04 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 054e0af7-e85d-3cff-8b18-17ec1aeb01b6 | -5.6963 | -45.6076 | 2025-09-04 13:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 93a49ad7-f550-3c5d-8274-8a951e033984 | -11.5779 | -52.115 | 2025-09-04 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 9d4b32d4-0969-3cd3-b020-eccd50ed87c5 | -4.9049 | -41.7696 | 2025-09-04 13:10:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 151.5 |
| 5af44092-6bbe-336a-ab99-37a8f7a8da04 | -5.908 | -57.7311 | 2025-09-04 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| c2675ab4-1059-3182-a079-17eb3022c0e4 | -7.6849 | -48.7602 | 2025-09-04 13:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 81.9 |
| e15d6495-3939-34ed-9f6d-0f527db8fb88 | -5.6777 | -45.6089 | 2025-09-04 13:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 179.7 |
| b32a760b-8baa-37b5-bdd9-a4e4af907cc2 | -7.7039 | -48.7371 | 2025-09-04 13:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 815ec4cb-9006-34be-a606-68a8b72bf4c9 | -17.0652 | -46.449 | 2025-09-04 13:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 3d03f1a9-7598-3a86-864c-b3c964d238b1 | -6.0232 | -46.6784 | 2025-09-04 13:10:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 095f64f6-e849-3a06-8670-3e010c9d3077 | -10.4658 | -50.3907 | 2025-09-04 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 0afb3d5b-3eee-312d-9905-7766694c563e | -4.9587 | -42.0761 | 2025-09-04 13:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| 15c9b624-dd7e-3be6-81c5-2d6dda8cf083 | -8.3641 | -48.3334 | 2025-09-04 13:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 4c0e4b0b-d8b3-3eb9-b1e7-3db6d983a3d0 | -14.9865 | -50.0769 | 2025-09-04 13:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 13aac1db-d69f-3c41-baf8-d24a67c2a500 | -8.0228 | -45.39 | 2025-09-04 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 57fa8f54-6f71-3ece-a9b2-0e8d6cc62bd5 | -11.6601 | -54.5093 | 2025-09-04 13:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 1cfa381a-adfd-3374-9d00-7892c0f7cbc2 | -8.9031 | -45.82 | 2025-09-04 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| c22ad0ad-9d68-3725-8b28-d15d1563d6ee | -8.3829 | -48.3317 | 2025-09-04 13:10:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 46519313-1632-37b3-84db-464cad666a23 | -11.5969 | -52.113 | 2025-09-04 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| dcbc8375-b1d2-3f8c-ba54-ee036159bb16 | -5.7 | -45.1786 | 2025-09-04 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 250.3 |
| a4c75e37-4aa6-33b6-938a-180876f3aa4b | -6.2315 | -42.4515 | 2025-09-04 13:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| 0b507494-8705-3546-a20f-88652cc1b00b | -4.9049 | -41.7696 | 2025-09-04 13:20:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| d4d64db3-3587-32fb-bd32-610bb7aa9ff5 | -8.9031 | -45.82 | 2025-09-04 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 276ce56c-2b6e-366e-b83e-4db5350402fb | -6.3692 | -45.6258 | 2025-09-04 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 8b3ef569-f8f5-31bf-8456-a8421d40a9b5 | -7.7409 | -48.7772 | 2025-09-04 13:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 6b931d6c-9681-37c5-b8fe-c9d8393ad437 | -10.9867 | -45.9325 | 2025-09-04 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| b1013893-d5d2-3536-b2fc-a8bcbbcba484 | -8.0799 | -45.339 | 2025-09-04 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 155.2 |
| ae2c41da-616b-3c8e-ac2a-292d9b09931c | -11.0062 | -45.9072 | 2025-09-04 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 011ae891-d09b-3f31-abcb-cb30f2851127 | -8.3829 | -48.3317 | 2025-09-04 13:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 42cb206b-7704-3390-b658-a35de93594be | -6.2318 | -42.4278 | 2025-09-04 13:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| d7421a69-d3b7-3e99-b8b3-7d38c2660194 | -6.0421 | -46.6549 | 2025-09-04 13:20:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| c72c5a92-13d2-3fe5-87a5-0eef1e7e01af | -7.6854 | -48.717 | 2025-09-04 13:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 3c2c4cbb-c30b-3790-97af-84884e73f434 | -5.0135 | -56.2553 | 2025-09-04 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 04d73238-6012-340d-97e9-7182c360308f | -7.6849 | -48.7602 | 2025-09-04 13:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a364055e-cb93-3e9c-966d-70a81f188c3a | -14.5855 | -53.0056 | 2025-09-04 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 5e14cee2-a123-3d8f-958d-2ffdcd3563d0 | -11.9635 | -45.7741 | 2025-09-04 13:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 8cd07f8c-71c3-3ee8-87e1-30a208f238da | -8.0228 | -45.39 | 2025-09-04 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e1896d40-5b1d-38af-b2fb-905b2b61e7b5 | -10.1457 | -46.2424 | 2025-09-04 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 3230c4e4-222b-3ce0-a99b-03f614015cf7 | -8.0796 | -45.3617 | 2025-09-04 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| ffdb764b-9dc0-3766-b509-dce7a2bf0fd3 | -17.0652 | -46.449 | 2025-09-04 13:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 102.2 |
| d496187e-35a0-31c7-9075-ab3681cbbe76 | -11.6338 | -52.193 | 2025-09-04 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| bc97ed52-ab9d-33b3-b93c-960fa87421c1 | -7.7036 | -48.7587 | 2025-09-04 13:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 5738ca9b-9461-3306-ba34-af5a6ac62394 | -10.4658 | -50.3907 | 2025-09-04 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 308dce1b-f001-3be9-8ee4-f5b4a44acbad | -7.7039 | -48.7371 | 2025-09-04 13:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 82.0 |
| e0752e0c-fe10-3ed6-9df1-87dac9671ce1 | -14.5852 | -53.0268 | 2025-09-04 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| c79d9a4e-1c15-3256-8e24-f3ae4a540461 | -22.6558 | -43.7079 | 2025-09-04 13:20:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 137.8 |
| 23801b3e-ae09-3edd-93cb-0326956025e3 | -6.1665 | -43.3273 | 2025-09-04 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| e26f8259-1255-3970-bce5-905c6ae75677 | -8.9028 | -45.8426 | 2025-09-04 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| bb1672aa-7e6d-3209-9072-44aaa48cc1da | -5.6963 | -45.6076 | 2025-09-04 13:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 528db196-ea51-34a2-b1b8-049417462873 | -6.0232 | -46.6784 | 2025-09-04 13:20:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| b14f4027-7728-34e8-9b7a-72c04b86425b | -9.6913 | -49.0089 | 2025-09-04 13:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f4d5bb8e-7249-3b8a-900a-d23c78199e0a | -12.2344 | -50.1488 | 2025-09-04 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e337d169-2551-3e75-8b2a-691a48601647 | -11.6231 | -46.6614 | 2025-09-04 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |


[Clique aqui para ver as próximas entradas](README105.md)
