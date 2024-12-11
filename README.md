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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d52b95a8-eed2-3485-a060-edfb1952f2ba | -3.3341 | -53.2523 | 2024-12-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 63ae480a-c7ad-3499-a8d3-221ed46f7271 | -2.9483 | -53.1003 | 2024-12-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| b31b5fa8-92d1-34cc-ae6a-e998b78c71b0 | 2.7627 | -60.6188 | 2024-12-11 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 925f7cca-3ac7-3099-8365-6b568ca40849 | -6.8972 | -43.4969 | 2024-12-11 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 98727a85-96d0-383a-b7ec-0bc5352249ba | -11.1295 | -54.6391 | 2024-12-11 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 58fb3b0f-af04-3fef-98bd-14773df3c30f | -18.0266 | -52.9614 | 2024-12-11 00:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 83311717-0b39-3355-a825-10b9eefe7c28 | -2.8197 | -53.0425 | 2024-12-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| b20e145e-9752-38f9-8950-049f2aef2a4b | -2.8196 | -53.0629 | 2024-12-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 7173b154-e953-3b67-a703-1e8749f3c2a6 | 2.7627 | -60.6378 | 2024-12-11 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 1043823e-6a43-39bb-b891-a47cf5df9615 | -6.9594 | -42.9759 | 2024-12-11 00:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.7 |
| 45eb12da-de44-3b5a-821b-fa06fd39c645 | -2.9482 | -53.1206 | 2024-12-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2de2f874-3654-3621-862e-2772777321c6 | 2.7444 | -60.657 | 2024-12-11 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 126.4 |
| cebfcc56-6336-3dd4-8ce6-92442dcfb375 | -3.0949 | -53.2385 | 2024-12-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 801931dc-b191-38be-9980-57297ae78980 | -6.9158 | -43.5185 | 2024-12-11 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 253d6f32-d793-3296-81eb-40fdbff0413c | -2.9666 | -53.1201 | 2024-12-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| abb5a602-a27a-3265-9b9e-c2f9e1a41cf8 | -6.9783 | -42.9741 | 2024-12-11 00:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.6 |
| 8a12d665-5c4c-35b9-920d-5e099700fda2 | -6.897 | -43.5202 | 2024-12-11 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 9101b354-dea7-3bbb-9a06-9e5aa04cdae4 | -11.1106 | -54.6408 | 2024-12-11 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| a65698f9-92ae-3c0d-b13f-9c3dacf9094e | -6.9403 | -43.0012 | 2024-12-11 00:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| 00f392dc-7a3c-31ed-a605-8f18e2a15db1 | 2.7444 | -60.6381 | 2024-12-11 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 178.1 |
| b5711ead-b346-3f9b-9e6e-588e4cb01bce | -3.1287 | -54.1054 | 2024-12-11 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 787aeeef-f3ba-3e6e-b629-edb66882fc1e | -3.1133 | -53.2381 | 2024-12-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| b2074d1d-7012-3391-8a87-ba6e4ef6fabe | 2.7627 | -60.6567 | 2024-12-11 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 86.1 |
| e0482610-7edb-3a8b-a9b8-e00b1199c338 | -3.1288 | -54.0853 | 2024-12-11 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| fe1a40c5-8452-32e3-8569-ab4516ad588e | -6.9592 | -42.9994 | 2024-12-11 00:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 193.7 |
| 13a453de-8eed-3880-8d2c-0ae8a1cdf409 | -2.9667 | -53.0998 | 2024-12-11 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 44a9c0ff-6cee-396b-a859-f4178215760d | -3.1471 | -54.0849 | 2024-12-11 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d50ca3d9-1974-3ac4-bd95-3c9ae9d90660 | -6.978 | -42.9977 | 2024-12-11 00:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| 102134ed-65fa-3c47-95b5-85573a940119 | -3.8165 | -52.3813 | 2024-12-11 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 6865fdc6-ccfc-3fdf-854c-99286d0be34e | -6.9161 | -43.4952 | 2024-12-11 00:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 84f69f49-bfac-3342-afcb-773dda32e222 | -11.1109 | -54.6204 | 2024-12-11 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| cf08b9f1-7dbb-3952-8a77-a7be04111734 | -15.971 | -57.1669 | 2024-12-11 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 377dbfde-09d0-3a87-b461-269ac7a6d896 | -15.0865 | -59.6487 | 2024-12-11 00:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c0a05d77-8571-3dc3-b0ff-bf2d3cffa99b | -3.1104 | -54.0858 | 2024-12-11 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 58f560c7-b976-3b2d-8406-e4e68b60ba98 | -3.2351 | -42.4353 | 2024-12-11 00:00:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 1a42b63c-6848-35cf-93e6-9a1dea5bd6b8 | -18.0261 | -52.9829 | 2024-12-11 00:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| c8776431-bfc2-3c8b-b868-77f45fb0b4e7 | -18.1192 | -40.1311 | 2024-12-11 00:10:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 105.1 |
| 98e62298-3576-3bfb-a5da-44553c092e94 | -12.5427 | -58.3362 | 2024-12-11 00:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| bc171724-10d5-317f-987b-3f457f5a1ffd | -3.1104 | -54.0858 | 2024-12-11 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3325fafe-2419-326c-8bcf-800b741777a7 | -15.971 | -57.1669 | 2024-12-11 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 513f4f30-bf32-3ed7-b0f9-34467c94cdcb | -6.9161 | -43.4952 | 2024-12-11 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 688e2030-f7a1-3804-996a-4aee4d540963 | -2.9666 | -53.1201 | 2024-12-11 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| b775498a-3aca-39e3-ac7c-764ab324ee90 | -6.9158 | -43.5185 | 2024-12-11 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 133.1 |
| ca94db4c-1090-302c-bf5c-f63dae1cd0d3 | -12.5425 | -58.3561 | 2024-12-11 00:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 7f672b4f-4e26-3be3-bf6d-00a6b4a3443e | -12.5617 | -58.3347 | 2024-12-11 00:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| d48cf027-db01-3e85-8621-2cd1d2cef2da | -6.9592 | -42.9994 | 2024-12-11 00:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| fe1860fe-e6d0-33b8-a6ac-e8247861d2e8 | 2.7444 | -60.6381 | 2024-12-11 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 184.3 |
| bdfd4212-d8b0-3819-8fec-e1c7e3b8cf23 | -12.5615 | -58.3546 | 2024-12-11 00:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 699ef175-e8c0-36df-8a68-59e195b2c2f9 | -18.0266 | -52.9614 | 2024-12-11 00:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 1caa3ba0-104c-3958-aa1e-b7565aebb05b | -2.9482 | -53.1206 | 2024-12-11 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 97ac5b04-399d-3acd-8e5d-318c10f28d6b | 2.7627 | -60.6567 | 2024-12-11 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 6dc2b3ff-8f95-3a17-a537-e026e845fac1 | -18.0062 | -52.9861 | 2024-12-11 00:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b5e7ab2e-829c-3902-987a-b8b8c1fb8fef | 2.7444 | -60.657 | 2024-12-11 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 90496c30-666b-3fec-80fb-4c4260c2774d | -11.1106 | -54.6408 | 2024-12-11 00:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.0 |
| fd090cab-0eac-3bb6-9fd0-93de557bef3b | -3.1287 | -54.1054 | 2024-12-11 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 7896e019-0796-3d25-9823-f2c64ce6532f | -15.0865 | -59.6487 | 2024-12-11 00:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6f1f40d3-7015-332a-b3c9-dcd9c7b13f06 | -3.1288 | -54.0853 | 2024-12-11 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 254e0c38-1e6e-3d77-bea4-7ee67f18b69c | -18.0261 | -52.9829 | 2024-12-11 00:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| aa766154-671a-39ec-b124-c4e7dc165713 | -6.978 | -42.9977 | 2024-12-11 00:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.9 |
| ca579825-2d67-3c77-a02e-653c30ba10dc | 2.7445 | -60.6191 | 2024-12-11 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f2c60293-de46-3de4-b23f-1717297b2c72 | -6.8972 | -43.4969 | 2024-12-11 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 140.7 |
| ac72e740-7e6a-3d85-9b66-6396d9002883 | -3.1471 | -54.0849 | 2024-12-11 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6a91f96e-5fc5-3963-92fc-1b78398077e7 | 2.7627 | -60.6188 | 2024-12-11 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| b96d77b6-6fe2-3f75-8e4e-1942c8afe5c6 | -11.1295 | -54.6391 | 2024-12-11 00:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 567d803b-e65e-3e1b-adeb-1222d3503c05 | -3.1133 | -53.2381 | 2024-12-11 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f2a1b410-267c-362b-a52c-b63ff1262bbf | -6.897 | -43.5202 | 2024-12-11 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 8491a5bc-d85a-38eb-ac04-af22668cdae9 | -3.8165 | -52.3813 | 2024-12-11 00:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| f3182361-4131-3ff4-9a5c-50a29de34fa4 | 2.7627 | -60.6378 | 2024-12-11 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 172.0 |
| f1791050-5d67-385e-a26b-c93b420a8a3c | -3.3341 | -53.2523 | 2024-12-11 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 72f6390d-8fe6-30ab-85fe-0c5148e4a397 | -6.9592 | -42.9994 | 2024-12-11 00:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| 2e866e99-2857-304d-90a2-53744e24de78 | -18.0261 | -52.9829 | 2024-12-11 00:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 02d73c98-2d26-34d8-aa99-3ea2c75e5964 | 3.2362 | -61.1982 | 2024-12-11 00:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 9d6184a1-8c68-3494-b0e4-1e581607ff8f | -18.0981 | -40.1629 | 2024-12-11 00:20:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 101.4 |
| abc8d4d2-9b21-3f08-a890-a93632d0ad00 | 2.7444 | -60.657 | 2024-12-11 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 118.4 |
| b37f89bf-c53d-3c56-97cd-efd6338f9e40 | -6.978 | -42.9977 | 2024-12-11 00:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 92548f1f-f759-3826-a17a-54b9627a685d | -18.0997 | -40.1106 | 2024-12-11 00:20:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 100.9 |
| dcabb128-5025-3b55-9f77-2f139e478a79 | -3.1288 | -54.0853 | 2024-12-11 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| d274d9a6-4ad3-37f6-88d0-2856fedff848 | -11.1295 | -54.6391 | 2024-12-11 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 934f184b-d0c3-38af-95d8-766c5e7f145a | -18.1184 | -40.1572 | 2024-12-11 00:20:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 117.3 |
| fde18889-7401-3f04-bfb7-e0d111da033b | 2.7627 | -60.6567 | 2024-12-11 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1b06ef58-562a-3e2d-a745-c8f142b2f333 | -18.1192 | -40.1311 | 2024-12-11 00:20:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 300.8 |
| 3e37199c-edc8-362c-9bea-efa538ac6f38 | -11.1104 | -54.6612 | 2024-12-11 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 97318c15-fae7-38d9-ad52-cd540e71d572 | -11.1106 | -54.6408 | 2024-12-11 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.2 |
| 9ca9cf9f-2cec-3eb4-9e00-9685b464264f | -3.1471 | -54.0849 | 2024-12-11 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f1435675-1f62-31c2-8e67-ba7f9207baf3 | -3.1287 | -54.1054 | 2024-12-11 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| a5960e75-cb38-3d02-8d21-816c4c14ab2e | -9.5316 | -36.0053 | 2024-12-11 00:20:00 | GOES-16 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 95.4 |
| 845da7a2-f2fe-30d3-a9dc-171087116f29 | -2.9666 | -53.1201 | 2024-12-11 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 1b70b757-bff0-3063-8c41-fa5ddab928e8 | -18.12 | -40.1049 | 2024-12-11 00:20:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 109.8 |
| 2da3cda1-1594-3260-bf95-21c8ce3017d5 | 2.7444 | -60.6381 | 2024-12-11 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 203.7 |
| a558bd1b-0ed6-3c34-96b4-12e2c7309b13 | -3.1471 | -54.1049 | 2024-12-11 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1b8d0889-097e-3930-b9fd-6ddf5c50fd0f | -15.971 | -57.1669 | 2024-12-11 00:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| f7779987-3bdf-3f9f-9157-a4b1803f802e | -15.0865 | -59.6487 | 2024-12-11 00:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| cc6e1e71-c3c0-3a05-b74b-f00b97e4ad62 | -18.0266 | -52.9614 | 2024-12-11 00:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 7e61b287-f2d4-32b0-9fa6-16c0f43fb8bb | -3.1133 | -53.2381 | 2024-12-11 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 7bd7257b-1d25-3d29-90c8-9b31e1bcc016 | -11.1109 | -54.6204 | 2024-12-11 00:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 57ad04fc-ed1e-3557-aeb0-4a7744619883 | 3.2179 | -61.1985 | 2024-12-11 00:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e9ecc19a-537d-37ab-9e11-86331f136298 | -18.0989 | -40.1368 | 2024-12-11 00:20:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 277.1 |
| 9822a7c8-3ceb-369d-922e-88eb348d8106 | 2.7627 | -60.6378 | 2024-12-11 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 153.5 |
| 4bb30029-07e0-3b11-b592-17212da1e541 | -2.9482 | -53.1206 | 2024-12-11 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 2300275b-3924-39d2-91bf-01ca6a5cba49 | 2.7627 | -60.6188 | 2024-12-11 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |


[Clique aqui para ver as próximas entradas](README2.md)
