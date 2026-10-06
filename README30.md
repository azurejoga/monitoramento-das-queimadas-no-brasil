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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 579ff7bf-b6a6-3386-ac13-483903362560 | -11.26795 | -45.50909 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| c363fb65-ec33-3ab3-9a1a-0f5f6b29e883 | -5.50602 | -42.80526 | 2026-10-06 04:19:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 10699e22-7e8e-383f-9b28-7b2494876df6 | -7.84783 | -42.92668 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 44976835-7bb2-3885-aa4a-65e3deb9d0f2 | -6.37356 | -42.5405 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8f1d2e93-9cb3-37b6-9830-0c5d2ebdab63 | -2.87743 | -54.1591 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9b800cda-c56a-34cc-bf24-13a58c752f1e | -3.06533 | -54.16984 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b536be7e-def9-3e5d-9f52-56285ca295c5 | -5.22638 | -48.39767 | 2026-10-06 04:19:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db86847c-43e2-30e1-9955-73d392be4839 | -3.06915 | -54.25257 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2cf5f4e4-da54-375e-837e-5d66a9578cee | -6.00662 | -47.39826 | 2026-10-06 04:19:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cb150945-9951-311b-b21c-2d3d68c86afa | -3.08747 | -54.16733 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7c023bb9-cf2f-3718-9842-ee7ec580a7b9 | -6.13457 | -43.1992 | 2026-10-06 04:19:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 10c87de2-fedd-398a-a9c7-356ad8470f3e | -3.4665 | -50.10528 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50db0ba5-3819-3c60-8750-18801d540868 | -5.41606 | -44.35098 | 2026-10-06 04:19:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cdbc3ff-ccc9-3f61-95d6-90e77af72497 | -2.93676 | -54.13262 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb1b9a8c-df37-342f-8ca9-2e02037e2c34 | -3.05996 | -54.22269 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4be71adb-e909-3e8c-9466-0133c92a8216 | -11.26229 | -45.52088 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5c622be-a106-3b9e-88c4-004d9d21bda9 | -9.88326 | -44.79995 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31a1461d-a335-3ba8-a53c-0b50fb66e156 | -8.58412 | -45.65706 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bc57114-194d-35e1-896b-39a9ad0b56a8 | -3.1151 | -53.75891 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 46f5e715-7b92-302c-95f8-be4b63d5a9a3 | -9.26359 | -45.66179 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c3083a7-8059-3983-8dcb-3552d66ff2d1 | -9.25695 | -45.65599 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41911362-8628-331e-897d-27bc3e6020c6 | -4.29254 | -54.79991 | 2026-10-06 04:19:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6c651eb-3a3d-3466-ae64-f942ef2b8c69 | -8.91191 | -43.88232 | 2026-10-06 04:19:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9e58714-e87d-3d63-9442-e0f630fc12a6 | -3.79892 | -51.03266 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca0ab1db-5ca2-3c06-aa82-2dc80b73f94f | -4.29023 | -54.80163 | 2026-10-06 04:19:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d9d4939-5206-35c2-96e8-aec58694a713 | -5.84541 | -45.02382 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 592f7255-dc73-3cda-b54a-057c33c57ab8 | -3.09653 | -53.7418 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4a89c98c-1954-35ab-8523-6358d96e9b03 | -7.37831 | -46.22129 | 2026-10-06 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 319b00a8-a064-3ef5-a2ac-dace43ec0122 | -3.27116 | -50.39791 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c11cb47d-f486-3019-9729-2f1ac5aea5b0 | -3.10138 | -53.75658 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 976ad205-3604-33ad-aa2a-3d05a732aaac | -3.06197 | -54.23129 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 06ff88ae-9dc1-35f2-ac44-3b10c15e2a1e | -5.68677 | -53.49027 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46da8a3d-432d-3856-81b4-41a61b76eb6b | -2.87283 | -54.14359 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 923551cf-1de2-3df0-be64-163ac2e5de6a | -5.95904 | -41.34806 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21835516-8038-3ba3-b417-8f8b809c65b6 | -6.37518 | -42.5518 | 2026-10-06 04:19:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 129cc4d7-4076-32f2-931b-844979a2adac | -11.66653 | -43.63309 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc594136-bb87-3515-826c-7e5c9ed0594e | -6.3984 | -42.79453 | 2026-10-06 04:19:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 40519a0a-ded8-3c95-aa8c-e24f9962dcc0 | -5.32276 | -40.89879 | 2026-10-06 04:19:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b457fe18-e592-3dbf-85da-2068e49b45a2 | -3.06541 | -54.25355 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4424d6ed-67ec-3307-a49a-20dc7b55c230 | -6.60962 | -38.66286 | 2026-10-06 04:19:00 | NPP-375D | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2318e85e-969f-34c0-9cde-1807362de6f8 | -3.73732 | -48.87262 | 2026-10-06 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34788f77-1984-356d-a14a-d962e4610c0c | -5.94631 | -41.36383 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a7109681-aa13-3351-939e-1eabc83dbb9b | -3.05609 | -54.22329 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8adf93fd-5c4a-3649-805a-fbcc4253d1fd | -8.27573 | -47.91826 | 2026-10-06 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93336583-0a38-3b0b-8a2f-268163647a16 | -2.87989 | -54.14462 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 83ff8166-8f97-357a-a34b-a9d60256e836 | -7.47203 | -42.80773 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 84b772de-7eeb-3017-a50a-e1afec874a87 | -5.88468 | -43.46272 | 2026-10-06 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 697e6561-19ee-371f-b93f-0ac874026584 | -2.94845 | -54.14863 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afd18e26-dbcd-3dd2-bedd-84cec3417bdc | -6.71864 | -45.97325 | 2026-10-06 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b569e225-8497-3bb3-b64a-b522fc1c760a | -3.02149 | -53.89153 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| fa83c86f-83ba-3d39-b082-3e84452d9f53 | -3.10109 | -53.7179 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ffe5eac-3702-34f6-a904-3b4668b99dfe | -6.62027 | -37.8917 | 2026-10-06 04:19:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6c8fa759-e1b6-3479-a2a8-9c8a152e2510 | -3.47031 | -50.09016 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caec32c3-52a5-3b23-97f6-8f124edf421b | -7.69651 | -44.62405 | 2026-10-06 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b722efd-1ade-3721-9eeb-9c122725f9d4 | -11.27084 | -45.51384 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 6591de48-fc2a-3cad-9fc5-30a2c694aebb | -8.69618 | -45.21468 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca88baf1-f901-3848-b130-1d8a886b1c96 | -3.02644 | -53.89994 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 0ddd34b4-3c77-30dd-8c8d-23cbba9eecaf | -3.12952 | -53.71649 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a70ac64-1b91-33a4-a072-a9e6588aac2d | -3.09877 | -54.16777 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2c8f5fb-ea12-3c11-b07c-1dfc7b870012 | -2.87 | -54.14162 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a6e2d2e-0368-32aa-bd8b-362a3dd10123 | -2.94261 | -54.14061 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2425916-a45d-3a78-ba6e-0004f08fb295 | -11.29095 | -45.51161 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b59b550-10d1-30cf-9664-e73e8d51f861 | -11.63502 | -43.65731 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b406569-2549-3841-9025-3203fc18ebbe | -3.46853 | -50.10042 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29e49e7e-f852-3fc3-a03d-24b0b41d26a5 | -11.27663 | -45.52335 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e79336e3-cdbf-3c8e-a4ed-b95cc4ba2ab6 | -11.29452 | -45.51229 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e92eb65-8972-3be7-b8be-b0f63c2cdaed | -11.29026 | -45.51569 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 79fd4ce0-f044-3f2d-82be-cf4aa525b200 | -2.99281 | -54.12961 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcd7fa2d-66bb-3cc4-88b6-a94cf25e75d4 | -5.61509 | -44.84585 | 2026-10-06 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8359b8eb-ce37-35a6-8ca7-0e74fc6cc25f | -4.45728 | -54.96807 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 56413415-8dc7-3dd6-9272-b0727e4e8988 | -8.69911 | -45.21957 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60ad20b9-3dbf-309e-82da-e9923211b4a5 | -4.77779 | -50.81251 | 2026-10-06 04:19:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bced6c5-2d6f-391f-b806-379009c1d414 | -2.77531 | -54.09476 | 2026-10-06 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7931b1c1-7ca8-31f2-bcf5-6fe30dbf656e | -3.49964 | -51.18719 | 2026-10-06 04:19:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 053f3f82-53d6-34cf-ab25-bcc2614d2861 | -9.82662 | -44.7954 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0212715d-28b2-3ed9-9e69-2d2cbbcf2407 | -3.00807 | -54.13842 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4111fc65-e065-3d0e-875b-96c826b7c454 | -10.97421 | -45.41922 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e0ecdec-a49f-31bc-9325-297dd0a2ac74 | -5.19018 | -48.31797 | 2026-10-06 04:19:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0425e3db-a9f7-34ed-9daa-705c0cadeff9 | -3.73235 | -48.87177 | 2026-10-06 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 512b26be-1304-33dd-9f20-c30cd2c8693a | -2.90171 | -54.08519 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43e3944a-ef7b-3959-acbf-61be3b6d3b09 | -8.70275 | -45.22019 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efbddade-427e-3fc7-9463-cf26c31f2ef2 | -9.79907 | -44.78677 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4bec93a-8fcc-3daf-aff0-9c0212a2caac | -5.83146 | -45.00987 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1b823879-e124-3d35-a4a7-e55f3952501a | -11.28738 | -45.51092 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 2f928051-03b6-35c0-a435-99d85bd9af43 | -5.95512 | -41.3083 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 93feb3f6-6f45-303e-8e73-1b245326ebf2 | -2.80257 | -54.13086 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fe07f2a-311c-307a-afb7-b0cce881840b | -3.0742 | -54.18373 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76c738bb-f7a9-3b89-8184-2c85493e4ba5 | -3.09231 | -54.18133 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 69b9d5ea-5280-3d2c-b8f5-4d24a67d7ef0 | 2.46056 | -50.83797 | 2026-10-06 04:19:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 281bfbf4-533a-32a0-87d2-3e18a7edddfd | -5.67794 | -53.49857 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a6f4692-532f-3997-9da1-33f02c467670 | -2.80477 | -54.13448 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e69eeae-ecb9-35d1-b31e-efaa8ebe0e8a | -6.421 | -43.46975 | 2026-10-06 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bab693d-84bf-364f-a96d-0e0b08dd5dec | -3.00686 | -54.13193 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e8497c38-825b-3165-8b2a-dac8f6bcd98b | -3.84354 | -50.31018 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 664c3e66-5f92-3153-96bc-9fbbcaf8d198 | 2.4613 | -50.84281 | 2026-10-06 04:19:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 679190af-6ab9-3f38-a1ea-cf9f5f168ee0 | -3.46914 | -50.09692 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b92790ba-3497-3f8b-8667-8391a9d87ffe | -7.38042 | -46.22868 | 2026-10-06 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34150f59-f638-35ab-bae8-0b656befd182 | -5.83447 | -45.01498 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| fd41d7c4-d18f-3364-a746-a7484a8d2f32 | -11.27938 | -45.50682 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 03293328-b560-3485-a5ba-e9fb2b376686 | -8.70052 | -45.21106 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README31.md)
