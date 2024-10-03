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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aab2d2b4-4047-3883-b2b2-c5256b3bf0ef | -7.75799 | -43.0625 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0c3ebccb-b5a1-3d1b-81ec-1969da75eac9 | -7.75493 | -43.0558 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 60625e73-d757-3dca-b1f9-d39a5c72cffb | -7.75336 | -43.05434 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 99afa8ba-32ba-3743-9962-8ce79195bb2b | -7.75239 | -43.06171 | 2024-10-03 04:49:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84043247-f05f-3e46-92a6-cb73e7224c5b | -7.70661 | -42.99164 | 2024-10-03 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e7b6f509-3b3d-3f29-a9cc-7dc84f94170b | -7.70099 | -42.99091 | 2024-10-03 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ee5cddfe-4f6c-35af-acd3-3924294d4ff8 | -7.69587 | -42.98647 | 2024-10-03 04:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0ea91497-374f-3480-8fa3-5efc418be26f | -7.69025 | -42.98566 | 2024-10-03 04:49:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 08b2c241-599d-36b3-84ac-d5c26a12d25c | -7.63671 | -42.46259 | 2024-10-03 04:49:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 65205add-3495-362f-8211-496362f49b9c | -7.63615 | -42.46679 | 2024-10-03 04:49:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f8184ea8-8b10-3066-967d-78c2cb7c313e | -7.29337 | -42.25908 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d219c63d-5a68-3b52-85e2-3f0e07592b68 | -7.2928 | -42.2632 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 89978bed-1f34-3381-95ef-aa2ae730b690 | -7.03579 | -42.81411 | 2024-10-03 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 700d2168-df84-3715-aba2-a3cdbf791ca5 | -7.02965 | -42.81715 | 2024-10-03 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 47a2d354-3d62-3b39-9896-e3618d58817b | -6.87794 | -43.60474 | 2024-10-03 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6df372dd-ae9a-3889-8996-927282255619 | -6.87749 | -43.60798 | 2024-10-03 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fdfdd71-958e-3437-af88-a3199ada5e67 | -6.87704 | -43.6112 | 2024-10-03 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26d677e2-883e-39eb-8338-ad718d5a7e09 | -6.87262 | -43.60388 | 2024-10-03 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6e80afe-96b2-3de2-af24-493a4bad667a | -6.87217 | -43.60714 | 2024-10-03 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26abf0cc-8aa4-38be-a769-a51702733586 | -6.87172 | -43.61039 | 2024-10-03 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc0211f0-0a3a-361f-887d-861e49cdca01 | -6.65792 | -43.13186 | 2024-10-03 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab236775-1655-31a9-bebf-b9972dae8e9d | -6.65744 | -43.13548 | 2024-10-03 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abdbb1af-c8fd-3717-a1e3-233725653854 | -8.31316 | -42.82713 | 2024-10-03 04:49:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1866df2-2220-3554-9cdd-949722e5d3ea | -8.31211 | -42.82895 | 2024-10-03 04:49:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 073c3ba4-0e83-319c-b0d6-a131bcc0c1f6 | -8.30743 | -42.82635 | 2024-10-03 04:49:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 853a4fac-3b75-3fcc-86a8-97fbd0dd4b7d | -8.30692 | -42.83034 | 2024-10-03 04:49:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7e6e2b70-8150-3fd1-b8c2-a2c01dfa61b6 | -8.30638 | -42.8282 | 2024-10-03 04:49:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a90b36b4-c98c-3abb-be91-ce1c63afb9d7 | -8.18306 | -43.69854 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c54a6f91-e098-3a23-a339-925b24ba4e8a | -8.1826 | -43.70208 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4c308122-a0ae-3480-98c5-e456bc023161 | -8.18132 | -43.69917 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c120d5e3-d347-32f2-8dcd-66954bbd452d | -8.16328 | -43.71056 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3cc6c914-3c18-3240-86c4-0b1211d05ccc | -8.16281 | -43.71399 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da9390ec-e841-3a1f-af84-b25e7760be2e | -8.16234 | -43.71737 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ce613b71-3bfc-3e74-a137-19045ac07403 | -8.15742 | -43.71322 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d95898c1-d6d2-371b-b7e1-a3db9a5cc9d5 | -8.15696 | -43.71662 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7e76bae2-a734-3613-ac88-98186dd1dc25 | -8.1565 | -43.72002 | 2024-10-03 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6e2ff120-0c73-3450-947d-45eb927e68b6 | -8.15558 | -43.72673 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a9d3c566-5de0-374d-8079-bc0aa5a1df47 | -8.18714 | -43.66727 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 863139c4-f02a-326f-b7ad-df10c9f1d93a | -8.18668 | -43.67084 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 884f9cb3-f49e-3a83-86f3-434451168745 | -8.1844 | -43.68827 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e8d35d4-830b-3ea0-9bb7-f22d8669e75a | -8.18396 | -43.69164 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c93cb294-59ee-3377-b1ce-45591a9b6faf | -8.18352 | -43.69504 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 661f190c-c434-35ba-90f9-7fa00f496e55 | -8.18274 | -43.68892 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb1fc8bc-fff5-3440-8d97-64d040b55352 | -8.18227 | -43.69228 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eba225ab-7cd6-307e-86e5-7b50cc81c898 | -8.18181 | -43.69567 | 2024-10-03 04:49:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a96da696-c473-3bfb-8e9c-d968daa82766 | -3.47124 | -43.35608 | 2024-10-03 04:49:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7103539b-a2ed-35a8-9705-8f238afe49a3 | -4.94584 | -43.68283 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40e2dbe0-a62e-3f7e-8e36-113a2a5451ce | -4.94067 | -43.68217 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 065a66ce-5b95-3206-a4fb-f2881580a257 | -4.9373 | -43.77755 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff13ece0-ab52-3e9a-a521-0354a8e419ea | -4.93687 | -43.78048 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c8f30eeb-ed25-3e5d-87f8-e2984fb63a91 | -4.93259 | -43.77398 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 837f681a-c8aa-3806-b951-abe9d22c7641 | -4.93216 | -43.77694 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 65d3c4e9-ffc7-30d9-84b7-96258ba1535f | -4.93173 | -43.77988 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a49e827f-0ff3-3209-af60-26a56dfdb993 | -4.92747 | -43.77327 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b0e3e12f-915e-3476-8e42-3171e407c353 | -4.92704 | -43.77623 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25a3d38f-9a20-3887-a6c2-183e52f0a867 | -4.92661 | -43.77917 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 20fe48a6-0d17-3961-9fde-f675044335a8 | -4.66553 | -43.76064 | 2024-10-03 04:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77f5fd8d-830a-31e1-b557-90ad717ff00f | -4.66376 | -43.75789 | 2024-10-03 04:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 984e4b24-ef6e-309a-8bc3-940a4f7d53c1 | -4.66333 | -43.76089 | 2024-10-03 04:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f84e4a1e-9dcd-37a0-a763-dfe49304c82e | -4.66088 | -43.75686 | 2024-10-03 04:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c1ada1d-15cf-3e1a-a9ca-a4b30f15fd3b | -4.66043 | -43.75985 | 2024-10-03 04:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 936962e3-1026-3b46-b8bc-c2ca44dc1b8b | -4.65866 | -43.75707 | 2024-10-03 04:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06435c76-78a7-3f05-a3eb-947841702b69 | -4.65824 | -43.76005 | 2024-10-03 04:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36415215-05a8-3675-ad25-115f30373440 | -4.54594 | -43.31044 | 2024-10-03 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab18edb6-c860-3e81-8960-2105290798e0 | -4.54114 | -43.30651 | 2024-10-03 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0a98b437-c0f4-33ff-ba56-60365194bcfa | -4.54069 | -43.30968 | 2024-10-03 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 0dcb7608-5002-307f-8b00-87c6b423505f | -4.54023 | -43.31285 | 2024-10-03 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 61c65590-e57d-3c1c-bcc2-e1a26b1fe82c | -4.53634 | -43.30257 | 2024-10-03 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 819c98f3-412e-3b4b-991e-43ecdf26104b | -4.53589 | -43.30574 | 2024-10-03 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c7782415-9b30-3b19-8bb3-e76ca45364fe | -4.53544 | -43.3089 | 2024-10-03 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 2b4f5980-d52b-3dc9-94bc-5643be7aca07 | -4.53498 | -43.31205 | 2024-10-03 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 15b18dc4-9bde-33f0-a2ab-aea8b51e8587 | -5.10439 | -43.32252 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5338dc83-d00e-35eb-9974-b012f21dafb3 | -5.10392 | -43.32579 | 2024-10-03 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee849faf-7e7b-3249-9b4d-054eee5ab8ab | -5.91366 | -43.96391 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26729cf0-f911-3735-9351-ef9c310167b0 | -5.91117 | -43.96246 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d5bbc81-2c02-3c62-af09-042ce3cdc886 | -5.90855 | -43.96306 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c3ff130-d66b-3d8b-b6e1-de699705b975 | -5.88539 | -43.72027 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ebd5829-ed53-3550-b070-23abd5e765f9 | -5.88495 | -43.7234 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdb04dde-aaa4-3790-8e0a-f940b803860b | -5.83605 | -43.95802 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 908f7819-8966-32dc-ab7e-d511058e6bbb | -5.83136 | -43.95419 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2808d82e-0cbb-334e-8201-a76758ca1448 | -5.72186 | -43.78837 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6b11baa-7ca1-30f1-9d9f-1f63fc281661 | -5.72041 | -43.78797 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7ad0b57-f1c2-3cb2-81eb-608a3e916c12 | -5.71996 | -43.79102 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6c5fc9b-6a8c-33a6-ac0c-653c88626459 | -5.71667 | -43.7877 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6648a98a-bb1e-3c13-a879-a75f9fecd353 | -5.71522 | -43.78732 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 352bac59-db94-3ef4-a8f0-6ba9f0192c02 | -5.71018 | -43.92942 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffd64551-210a-31f3-93b7-910ec3e9c6d6 | -5.70795 | -43.9264 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f13a9d47-503f-3f52-9627-516e9edd9823 | -5.70753 | -43.92939 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11abca49-04ca-392d-a644-2a6d843225d2 | -5.24759 | -43.81002 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abf85331-06b0-3eda-a00e-be7a05afad45 | -5.24333 | -43.80319 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dccd40d-ac3a-3fcd-a9e0-f913f5d0e837 | -5.2429 | -43.80621 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14ec05fd-304b-3ec2-ab61-90cef14823c8 | -5.24246 | -43.80925 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60f283f4-f240-387e-973c-1acf1b93664f | -5.2382 | -43.80242 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46227aeb-ab5f-33bb-a1a9-60d42fa41796 | -5.23777 | -43.80542 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd6db014-8a1e-352f-9a3d-4c385088c04b | -5.23734 | -43.80846 | 2024-10-03 04:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 418fa9f7-2a14-3e03-98af-dfda4e975dbf | -6.39542 | -44.75164 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40bba47c-86db-3940-8747-7237883d098e | -6.39056 | -44.75072 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d8659c4-5faa-362f-b9ba-0fc4a64c2bc8 | -6.26705 | -44.72909 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92861db7-fa33-3370-ac2d-3f084aa2a3f6 | -6.19592 | -44.12199 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8ab65f9-e378-3adb-9926-79d8d6c2bcb7 | -6.19552 | -44.12474 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README113.md)
