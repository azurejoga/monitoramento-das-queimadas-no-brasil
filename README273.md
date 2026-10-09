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

## Dados Diários - Página 273

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57b7555f-b50f-39f1-85c7-20235d209623 | -7.01526 | -47.68382 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 7cee6979-d681-317d-86be-9e1004d1d788 | -9.11977 | -45.83214 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 87901796-a927-34be-b53d-12e6d15f627e | -9.91321 | -44.85596 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bf5e358f-cb0a-3579-be06-5706c407cadd | -11.05636 | -44.03156 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a94a6137-8ea5-356c-b422-05d9a179f264 | -7.64304 | -45.39019 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 15fb93f5-811e-3c94-b6ad-bfcf8b444b7e | -8.97183 | -45.12728 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 69509f9a-4c11-3b83-8a26-7f04e687852b | -6.82031 | -35.02138 | 2026-10-09 16:01:00 | NPP-375 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 122f62fe-0823-337e-96cd-1b9b2ed7ce1e | -7.01717 | -47.68578 | 2026-10-09 16:01:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8d1effcf-4dca-312f-a7cc-15a5b4cd4e95 | -10.47051 | -47.2057 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| da831122-bf12-3ac7-bc7a-c7dcc9b9a46c | -6.02402 | -42.44281 | 2026-10-09 16:01:00 | NPP-375 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 460b1957-4730-3e35-9f84-c79e51eedf1a | -5.87949 | -43.41221 | 2026-10-09 16:01:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 881713b6-10de-3689-8341-804f413dcb99 | -6.88771 | -45.03323 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9923413e-879e-3b00-8bc8-46172c7bb49e | -9.97342 | -43.56921 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 77384ad2-d81e-33de-b808-80c99e4f4066 | -10.31742 | -46.29163 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e271c462-2c94-38d0-868d-d7cdc275d49e | -11.18046 | -45.30344 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a040b15-e539-3ecc-bd1d-1c774deb4aba | -6.92758 | -43.08546 | 2026-10-09 16:01:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c2bdb59a-1399-3386-a541-6448514ae0cc | -9.72137 | -45.69753 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 41b26dff-9d11-39a4-82ae-a0ee6b801cae | -11.00359 | -45.40996 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7c7ab638-5fd7-363a-92b7-36aab3cb68b9 | -8.07368 | -39.99736 | 2026-10-09 16:01:00 | NPP-375 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9a01f370-2549-30bf-8f48-60b5570cde44 | -6.58988 | -44.29502 | 2026-10-09 16:01:00 | NPP-375 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1988e4ba-35d0-3c8f-8915-ef84a6973aab | -7.85665 | -44.96531 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bda5bec9-951e-3b45-b49f-9822842a191a | -9.91796 | -44.78291 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| da0a0938-2513-32e0-b109-f5777ed6f054 | -6.57086 | -43.04697 | 2026-10-09 16:01:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fb051c21-8790-348d-ba2a-ebc001bc4ccd | -9.60587 | -45.98935 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 147c7b57-46b9-39c2-8e82-14d4cbf35bb0 | -5.50479 | -43.062 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4427d3dc-35f5-36dd-bc57-3b52ebc4d931 | -7.08267 | -44.04021 | 2026-10-09 16:01:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2baa1121-3f87-3d61-916c-d36919acc902 | -6.01053 | -40.97285 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 09fd38ce-c8a6-3568-901b-81c5eee3f0f3 | -5.23795 | -40.57738 | 2026-10-09 16:01:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8af77172-ef73-33fa-a8fe-7c82733099d5 | -7.01601 | -45.31392 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ddf0dfde-22ef-357d-a0d4-b62ab3b1f3f9 | -10.53263 | -47.30888 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5b7cc769-6bd6-3cd9-a16d-38ae39eed6c7 | -9.88831 | -44.80444 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 45.7 |
| e33f2f95-037e-3b0c-80e2-d669a1974ad8 | -8.5337 | -46.89365 | 2026-10-09 16:01:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1bace82f-2916-3973-82bb-fd7e675f5731 | -11.06555 | -44.1074 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 200.6 |
| 30a925ab-c9ba-3f36-8e07-a68456868f6a | -11.11909 | -44.0163 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 73064c6d-66e7-300e-bf3a-4757e372abd1 | -6.94204 | -43.66346 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4d8ef421-c164-329b-8a6c-a5405238d435 | -7.47702 | -42.84557 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 339dac28-fe7a-3b34-ae31-efcc05107783 | -11.11434 | -45.68006 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b4b511e6-6f38-339f-8c8f-57df48d54cd9 | -6.05933 | -42.58873 | 2026-10-09 16:01:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 49cdd849-428d-33b3-a445-c7dd12d6f9d5 | -6.01437 | -40.96809 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 51aca890-06f7-34b6-9ae8-1c772c74671e | -11.24922 | -46.32703 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 20248a4f-ef3e-32eb-87d5-293dbae86a7d | -5.75613 | -41.68542 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| def25b74-debb-37f3-bb63-bed70b6e3fd8 | -5.48595 | -43.03827 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9d13e5f5-5f29-33cf-aa24-8f0227fa386f | -8.30037 | -44.16289 | 2026-10-09 16:01:00 | NPP-375 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9e597a6d-53b3-3d23-a4d3-df0c15adc36a | -9.98719 | -45.9285 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 240caedb-fe3e-337f-849c-a6138d042e60 | -6.738 | -43.0679 | 2026-10-09 16:01:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e9cd333-8c04-37bb-8be5-fefecb1c4623 | -9.83755 | -44.7914 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 84235fee-2699-33d0-a372-b0ab84961b64 | -9.88774 | -44.79986 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| d0398944-725e-3f59-a720-c97e897e8b31 | -10.32961 | -39.48785 | 2026-10-09 16:01:00 | NPP-375 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| d9a71d19-14f0-3430-82bb-afd307d95f85 | -11.25942 | -45.24856 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| df28a6f2-bdc3-3e3c-b564-d27e2a8f5925 | -7.29202 | -44.01954 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 131146ec-2310-3094-aada-6991055a88dd | -9.18912 | -43.3833 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| b091c352-cebb-380c-b4ad-51ba4a06ca15 | -7.37895 | -44.03471 | 2026-10-09 16:01:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 57adc686-c60e-33e3-a7d8-0142df897ab8 | -7.5059 | -45.28999 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0b4df9b3-e4dc-3e75-822e-43edf91c48a5 | -6.00932 | -40.96417 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 7a69b202-9140-32c7-b21e-866cd2739228 | -8.93631 | -45.14097 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 88a7188e-b9be-3be4-8a66-1bc9f574b447 | -7.15845 | -44.50172 | 2026-10-09 16:01:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0cc2d2f3-e94b-3e88-9118-00774f65a220 | -6.00549 | -40.96901 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 37.5 |
| 9fe88e4b-a386-338a-b63d-a7dd8714e72b | -10.45231 | -47.2981 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 16b907ca-3d76-3039-9251-241850e17737 | -5.18024 | -42.68585 | 2026-10-09 16:01:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aa28d9c9-f449-331e-8b13-3af184c523e4 | -9.98686 | -45.97871 | 2026-10-09 16:01:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 44bf1a38-7e01-3c17-bb26-4cab4bf2d12b | -5.45818 | -42.36467 | 2026-10-09 16:01:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0e98fe3b-7972-3851-9f50-567a7cd5f833 | -10.50963 | -47.23473 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 10e6f304-aaf6-3389-af9a-2323dd5aea85 | -6.68757 | -41.75848 | 2026-10-09 16:01:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 4b7946d8-cc0e-3417-b930-f92755fc8142 | -10.62354 | -45.24198 | 2026-10-09 16:01:00 | NPP-375 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 59285de5-d882-362f-bf80-dcbdd9addef3 | -10.91517 | -45.38479 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b762b423-69d5-3b5b-8640-188dbfac1ec9 | -8.66497 | -44.87793 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 3c1809a4-f878-317d-a6f4-f1d8f3c15a1c | -8.98295 | -45.90355 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| eaace93b-7e18-3d65-980d-87152c59f1c1 | -7.79391 | -44.57256 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 639341bb-1932-30d8-a48f-7a91ac324520 | -11.08165 | -44.09257 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8aa22096-3815-3aed-bb75-35c9cb5f764b | -7.47714 | -41.17092 | 2026-10-09 16:01:00 | NPP-375 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 746e4c0c-424c-32dd-b358-84b4d54b04b0 | -11.05152 | -44.04067 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 805defeb-2023-3910-8a6b-617520406a44 | -9.0206 | -45.94328 | 2026-10-09 16:01:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ee1ead71-f2fd-3ee6-96e5-980db0f65ad6 | -11.07681 | -44.10174 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| b755061e-03c4-34bb-a7e9-629c6c288bb5 | -8.91415 | -45.16601 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 89f332bf-cd68-3ca0-b6d4-1aba8ce164b0 | -6.00963 | -40.9632 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 92e76baa-cd52-34b8-ae80-1ab5eedebb4d | -5.15025 | -39.50539 | 2026-10-09 16:01:00 | NPP-375 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 7c8c8292-5f13-30c0-a62a-eaea9b836e28 | -9.91678 | -44.78634 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| fb142cfa-b8c5-369a-b629-f0a83e55e916 | -7.03628 | -42.30065 | 2026-10-09 16:01:00 | NPP-375 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0125334a-192d-3503-af53-86fa3abb4105 | -8.18697 | -44.42049 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c951dff3-96b1-3ddf-a4d3-a8d7d7e52d7b | -8.31723 | -45.74666 | 2026-10-09 16:01:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc487ce2-1a85-3d50-830b-3bb393de2d5f | -9.74075 | -45.68722 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2120b352-b060-372a-82e7-da27754aa709 | -6.77986 | -38.2621 | 2026-10-09 16:01:00 | NPP-375 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 14.9 |
| a89a2e6d-595e-3d71-9234-2cbfc16e777e | -5.6095 | -44.12218 | 2026-10-09 16:01:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 21384994-0f67-3a7b-b630-5310fb85c1e0 | -6.36796 | -42.90064 | 2026-10-09 16:01:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 68b43f37-c4b2-3b7f-ad8b-b573db034ab3 | -10.47422 | -47.23823 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| ab095a76-db1e-3901-b7db-e5d47b98cbca | -10.48436 | -47.26422 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| ea64c241-5975-3c37-a836-c8da60b6517f | -11.26334 | -45.20137 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68290bdd-d539-3b47-9c9e-5a4bc72ea9c6 | -7.07671 | -43.50528 | 2026-10-09 16:01:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2074246c-fb8b-3faa-a666-07b5a80fe0da | -9.83119 | -45.78871 | 2026-10-09 16:01:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 287dca93-170d-311f-843b-babb7008c1d3 | -10.88099 | -44.79409 | 2026-10-09 16:01:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f516a035-6564-3831-ba5b-05fcbd2001a9 | -6.80616 | -41.23716 | 2026-10-09 16:01:00 | NPP-375 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| e19d2135-33da-31bb-bb8d-658cb4a319dc | -7.82394 | -45.49041 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c53e23fd-c998-3863-a4f6-806f1a9bb477 | -6.15212 | -47.91894 | 2026-10-09 16:01:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5c115427-17c7-3b9d-89b0-50969bc54a9c | -8.32822 | -45.00831 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 3433e42f-247a-3e2c-bd75-4cb5f81846e1 | -5.24424 | -42.66331 | 2026-10-09 16:01:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 65955512-8f60-371c-bf73-62c0c030c95a | -10.61802 | -43.27884 | 2026-10-09 16:01:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d576c8be-214b-3f43-9168-9a1c98a3558a | -7.49435 | -42.81886 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3b6e851c-341f-38a2-9a68-b02aafb76cd1 | -6.02477 | -42.4482 | 2026-10-09 16:01:00 | NPP-375 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5fea6a68-508c-3ced-a53a-5cf009f39587 | -9.15855 | -44.7873 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 541b4e7b-061d-3252-8e88-20bc2f3e0da0 | -4.57638 | -40.66602 | 2026-10-09 16:01:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 25.4 |


[Clique aqui para ver as próximas entradas](README274.md)
