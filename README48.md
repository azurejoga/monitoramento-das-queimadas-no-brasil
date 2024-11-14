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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52f6774b-652e-3f93-a9ab-960979ee690b | -1.40755 | -52.38657 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e6d6aa78-49e1-332e-8a8a-102028177a1a | -5.08438 | -45.98419 | 2024-11-14 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fa6f4e4b-2788-3614-a3d4-02fb41fffc59 | -1.34027 | -51.43116 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6d7f729-963b-3f5d-bef9-6c4dc85842f1 | -2.65277 | -46.17697 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba1c814e-0c81-35f1-a00e-8f55ebab6ed9 | -0.97559 | -52.37994 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49ddade4-4896-3a26-a907-238a4b2b36ba | -1.56998 | -52.01781 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4026e8e0-4aa0-36d9-ac48-76372f25dfb6 | -1.55907 | -51.85475 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32e0d86b-c89d-3d55-9edd-3a89eff07ad7 | -1.39676 | -51.1169 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c22cc1d8-9591-3a25-b426-2b47f9075132 | -2.08536 | -47.73606 | 2024-11-14 05:01:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 99d32e96-0ab4-3eff-a625-df1c0dc5eced | -3.17154 | -50.45216 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3d716b7-42cf-3327-bc5f-f344b93e304c | -3.40438 | -50.30853 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75c0a9ea-8383-3a23-bbdd-2ebe7bb9f80c | -5.55264 | -44.32541 | 2024-11-14 05:01:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb89ba5a-57aa-3628-904d-ec1d00e7676d | -1.21697 | -51.78555 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2baafd53-c2c3-37e0-93e8-d83a0a779f3a | -1.39174 | -51.12491 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25b711d5-788b-3f10-9f93-fdc3cd4405a5 | -2.15359 | -50.715 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d93ebdae-8294-3a8f-abc8-8d1647e80dcd | -2.8984 | -51.79397 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa879f1e-3d51-3e94-b2d7-aa8c62da0783 | -0.19748 | -51.5042 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa837a06-327b-3d7f-88cc-6703fee2b034 | -0.91254 | -51.7256 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cec3f6b-bc45-3ba1-948e-6f3e7c65600e | -1.79817 | -52.17128 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 119e50aa-5310-3dd9-87fe-4735657f0ce6 | -1.20759 | -51.77598 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa4cfb67-5cad-33f7-9609-280906e79d3f | -1.28609 | -52.47261 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 135a375f-606c-3061-a998-3dada69b05be | -2.11873 | -50.69318 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c8e657b-5389-3799-8050-ef93b657ef48 | -2.20921 | -53.75126 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79439b63-286a-38e6-9805-879272b4133a | -1.26745 | -52.17206 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 212d26bb-358b-3a59-ac2a-8120221ebf00 | -0.18619 | -51.50652 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9994c6df-f347-37df-a85e-246d8c591374 | -1.46915 | -51.1307 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7c4c7ce-9166-3695-b662-edb6b8ab3d7a | -0.18974 | -51.50708 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e699fe9d-f135-3019-9935-cd00fa5c214f | -3.67038 | -50.16064 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34081ce2-b276-3b5c-90db-1dcefadb9faf | -0.90254 | -51.72 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c5dce63-4722-3c4d-b845-fcace8735169 | -1.6306 | -46.10526 | 2024-11-14 05:01:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ff88cbc-880f-36e3-a081-b75441ccf7c4 | -3.79905 | -44.85518 | 2024-11-14 05:01:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a80072a8-6aa2-332e-a0ee-f7ca204c4b3d | -1.63805 | -53.27602 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d64cf6d9-af8b-3479-a19d-388d2ceb0a5b | -3.23466 | -50.67285 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7db5d81-d5d0-3497-a5ac-a17802ad7731 | -3.90473 | -50.08877 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 698f1a92-a2c1-3a70-875d-b3106f5131d9 | -1.39119 | -52.0759 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a930779-4995-38a7-b498-c464d2aaee62 | -4.40171 | -47.26953 | 2024-11-14 05:01:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31d94c39-ca79-36ee-98d1-0ff38ed9adff | -2.88832 | -51.69064 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 026c7873-3c60-32dd-832a-3bbeca057141 | -4.14965 | -45.77203 | 2024-11-14 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9fee41bd-f56e-322e-9f50-c417fe4e9002 | -1.38834 | -51.55901 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12fbbbfe-fd4f-3653-a0f3-d6d42d9334e6 | -2.78246 | -50.30398 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d63c3a30-8247-3474-a1e5-a359e07ed323 | -2.66831 | -46.99411 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 40b77bd8-cc01-39a2-9a9d-0236486b14f9 | -2.88269 | -51.80007 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fa7b30a-9755-3082-87b3-c808bf8de28f | -1.61745 | -52.51833 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1ac8a64-db2f-3983-a296-62456d1306f0 | -3.76907 | -47.48666 | 2024-11-14 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8787a32-e76e-3061-86b5-7bfb34c50607 | -1.84305 | -46.28582 | 2024-11-14 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa21b63e-9e21-39db-b56b-8d6f69fd30cf | -2.64275 | -46.16561 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48735a56-f433-3a56-abff-90df29dcbafb | -5.36393 | -44.94214 | 2024-11-14 05:01:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f1d4723-8207-3818-9ff7-967b11873eba | -2.74847 | -51.96844 | 2024-11-14 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3afe7564-492e-37b2-a432-6acb201861ba | -0.91734 | -52.57253 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca190542-5bbf-3c5a-96e0-6b3be9f857da | -4.13494 | -51.07404 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8347c4f-28af-3374-9d20-071c70f60396 | -1.34117 | -51.40166 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17479b4f-a50d-3b62-bb08-6d916f9d7d59 | -4.44388 | -45.94931 | 2024-11-14 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47c7e733-863a-3fc8-85c7-14d083864c2d | -1.38287 | -51.5707 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d760b266-2756-3b6e-83d6-52c082b20c95 | 0.00371 | -51.13091 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb545c0e-acd1-3315-982d-a62689b962f7 | -2.27548 | -45.34289 | 2024-11-14 05:01:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3e49d6cc-e32f-35b4-a4a1-3b4c10e23d28 | -0.8336 | -53.04292 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1746212e-f6c0-3c97-8fcc-2edea37fd547 | -3.41356 | -50.31333 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 767dfd9f-f749-3a22-88b3-3f2d6a432ffe | -9.16115 | -50.54077 | 2024-11-14 05:03:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df841a07-eee3-3e03-b241-eabf53f4d587 | -9.16172 | -50.53679 | 2024-11-14 05:03:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ffbe867-ae72-3bbe-9bbd-5d39e8b87edb | -11.46582 | -48.00971 | 2024-11-14 05:03:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f23c0e8-93ca-3be6-946b-183d33c4e2e5 | -11.46543 | -48.01286 | 2024-11-14 05:03:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca143fa3-586c-3591-8111-5bb5cc6f308d | -9.16539 | -50.54135 | 2024-11-14 05:03:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe708d50-aae0-30b6-b0f8-d81cf8572c54 | -11.46061 | -48.00897 | 2024-11-14 05:03:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75ae2169-1c18-3b73-a1e1-cb93d54e376c | -15.93743 | -59.27635 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b2a7e9cd-a0a0-3031-8d5d-95c11c4a29fb | -15.87694 | -59.28487 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e160717c-8523-3c57-93f5-cb7f65d7f1cb | -16.09899 | -60.09661 | 2024-11-14 05:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 91965c07-dd47-3c55-8f5c-c60e26cef5b1 | -17.59263 | -57.47913 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 8635fb9c-4f60-3718-aa71-ef70dc1597a3 | -17.5775 | -57.55539 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.3 |
| 40daac2a-3a85-3b07-89dd-e0926fd334da | -15.87572 | -59.29229 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b719c4b8-7aeb-36ed-a24f-4d8a1a670671 | -15.87233 | -59.29174 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d437408a-b77f-346e-a26a-dd53b1a4f8d9 | -15.88586 | -59.29407 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1dfbeb8-e8c7-3b2b-bc2f-4cab31b77344 | -17.28726 | -57.30902 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 33f9f021-3a53-36a7-9b57-073fb4a5cb91 | -17.59653 | -57.47602 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 7980082e-e5ad-392d-a39b-357f754e8bf6 | -17.26761 | -57.48205 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cc204387-4467-3508-96ed-bafe43e65c73 | -17.26983 | -57.4899 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3fc11a91-460d-3e0a-b156-4a5525b814b7 | -17.26037 | -57.48458 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 27367b05-2bd6-367f-a636-f1e68224d705 | -17.59597 | -57.47968 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 45073651-2e37-3f93-8c51-66db3d657e50 | -17.59206 | -57.48278 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 15a2608f-ead4-329e-804f-5c837df24d0b | -15.88248 | -59.29345 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8736bd15-ece0-38bf-be8c-886a10bdf68f | -17.58977 | -57.54244 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5fc4c773-c4f5-3a04-9f6e-2afd0df833f6 | -18.72445 | -55.57894 | 2024-11-14 05:05:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ac0ed11e-b91e-3920-9b2c-36a38a6c6c71 | -17.60257 | -57.54833 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 84288dee-1baa-3e88-868c-ae6b4031884f | -15.89507 | -59.28032 | 2024-11-14 05:05:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d6e21aa-40b0-3d65-b9e6-0895ab4f3b0d | -17.69452 | -57.54057 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4c27f42c-e79f-349f-b081-674182be5e2b | -17.59319 | -57.47546 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ba375ada-01f2-3e56-be75-76754f0f7387 | -17.59707 | -57.49488 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| dea79493-79d1-3312-b3e2-974d14d36651 | -17.67727 | -57.51891 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8751fed4-36fa-3aea-bb9a-2ab63aa85d13 | -17.60097 | -57.49179 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 794c2fdb-e5e5-39cc-9500-1d3a637ce8b8 | -15.8751 | -59.29602 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| dcdfad99-822c-33e8-8dd5-b3738430e603 | -17.60322 | -57.47713 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 378c3788-ff43-331a-854b-9654e07f6e46 | -17.24145 | -57.47395 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2295788f-4d13-37bb-b379-ffdaa703a6e9 | -17.5714 | -57.52813 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 4bbecc18-8d89-3e1e-afed-d964ecd8ad88 | -17.62652 | -57.54858 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d12a2595-2001-3dfc-b5c6-6c3a37368b85 | -14.49988 | -56.9156 | 2024-11-14 05:05:00 | NPP-375D | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f41c264e-6c96-3b19-b3be-7de5fe6269e2 | -17.28709 | -57.48904 | 2024-11-14 05:05:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1f699cb9-76f2-380e-b553-9496290221d3 | -15.31144 | -56.51653 | 2024-11-14 05:05:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d05d05e-8a2e-3e66-b5d1-ad99b7fdd9cd | -16.00844 | -59.39941 | 2024-11-14 05:05:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3279283-acde-32f3-bd1c-5f4339e5a36e | -17.62374 | -57.54436 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 61501eae-4934-3656-84ef-4c9241efef62 | -17.71067 | -57.54702 | 2024-11-14 05:05:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5627b5da-6d69-3a0a-b80d-117bf375b19c | -16.0338 | -60.04962 | 2024-11-14 05:05:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README49.md)
