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

## Dados Diários - Página 389

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7a94026-1626-392d-8e8d-1a3d10afe292 | -6.0074 | -53.5325 | 2026-10-08 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 998c080b-0689-3cad-9a11-a225a52b68e8 | -7.4697 | -42.8315 | 2026-10-08 18:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| d405aa2d-f7ce-3d23-8565-98bb1c5f9f7e | -9.9208 | -44.7893 | 2026-10-08 18:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 532185c1-b346-3846-9e2d-39ba0271b278 | -3.1951 | -42.9538 | 2026-10-08 18:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 49a0c904-a7cd-3611-8f14-850c779eff04 | -3.2085 | -57.87 | 2026-10-08 18:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 8ba2207f-4cf0-3c0e-a001-be825aff140b | -13.1639 | -54.3385 | 2026-10-08 18:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 368.5 |
| 2ed1f19f-ba24-3df2-89a0-d71972f3c787 | -11.4503 | -43.4091 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.9 |
| b0fd4cdd-6842-31e7-a22e-bd0e37a48cb4 | -7.8257 | -44.565 | 2026-10-08 18:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1e2301bc-b3dd-3499-97ee-507b348d4e65 | -9.3394 | -65.4638 | 2026-10-08 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| a16a3dd0-4d10-3c12-bed7-1d3342836f19 | -2.572 | -56.1646 | 2026-10-08 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 250.1 |
| 650d7821-c3c5-3ce8-bca3-9db9681b7ae5 | -11.8503 | -43.5598 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 47261dd4-84d8-3bab-a756-f681858d6066 | -2.5721 | -56.1449 | 2026-10-08 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 2bb28ad9-a2d2-379e-bff6-70316d9cd9df | -3.4312 | -56.9502 | 2026-10-08 18:10:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 7bd51c55-6eb5-3e47-9b63-842ddd42f3d9 | -1.5306 | -54.5359 | 2026-10-08 18:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 3ccff494-ba71-3ff8-b669-5b7c0964584a | -5.6932 | -53.487 | 2026-10-08 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 203.0 |
| 8778c216-2570-3e27-b65d-0bee55e09cc1 | -7.0892 | -52.6753 | 2026-10-08 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 94b4b01c-b006-3642-acce-96305e5577bb | -6.9331 | -43.6566 | 2026-10-08 18:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 139eb224-88e7-35a4-a273-f325f27fef82 | -3.7239 | -57.1384 | 2026-10-08 18:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 18e692af-ea28-3570-80fc-1118ca9426e5 | -4.1023 | -44.1379 | 2026-10-08 18:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 97539362-d977-3b09-b469-488bbced009b | 1.7121 | -55.6063 | 2026-10-08 18:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 792bb982-3ab5-3924-be1f-dca9ae9eba6f | -8.6133 | -44.896 | 2026-10-08 18:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 6a7e0344-d592-3b3d-9f64-6ba022da1d54 | -3.4277 | -58.0397 | 2026-10-08 18:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b8ea710a-2d57-3502-ad42-c50e797dbfe8 | -2.4806 | -56.0875 | 2026-10-08 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 69a5035e-45b5-3d1a-8f2b-047013a33bf6 | -7.184 | -46.5225 | 2026-10-08 18:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 6e8af353-be12-3858-aee0-f7056b2982c6 | -3.1115 | -53.7637 | 2026-10-08 18:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 4c9ce050-c1cc-3dac-a58b-07ff5aecbee1 | -2.7613 | -54.0941 | 2026-10-08 18:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| e41c87c6-1a65-39ee-be03-e5685cf0c2fb | -4.576 | -40.657 | 2026-10-08 18:10:00 | GOES-19 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 110.8 |
| f1382746-8397-36a9-8b69-32bba04919a7 | -3.2451 | -57.8693 | 2026-10-08 18:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 6325fa58-041b-3184-ae17-ddbcf6c60c06 | -6.3134 | -54.7884 | 2026-10-08 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| bbd12d8a-44dd-33dc-a1df-7c995435b690 | -12.0444 | -43.4578 | 2026-10-08 18:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 22601c45-d598-317c-abec-dbbb998b2c2b | -8.6136 | -44.873 | 2026-10-08 18:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 2a0a3a1c-3450-364a-b21c-9b4ed15b9bc8 | -2.3115 | -57.9829 | 2026-10-08 18:10:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| fc352b32-81eb-36c9-81fb-f81631c5ce30 | -6.1747 | -53.4224 | 2026-10-08 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 6d8a4f29-9f3b-3485-9350-39b9008b3a2e | -6.3133 | -54.8084 | 2026-10-08 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 6b7f22a2-c9fc-323c-9b70-20c434853005 | -6.6899 | -45.3746 | 2026-10-08 18:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| fa010fcd-85f3-3a2f-b9ea-c8ca94dd8959 | -2.9265 | -54.1104 | 2026-10-08 18:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 06e2978a-5309-3654-8cf8-2eb6535b95cc | -6.3232 | -46.5459 | 2026-10-08 18:10:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| bcfdf157-daec-39ca-8cf5-5291aaeb7210 | -2.8433 | -57.4891 | 2026-10-08 18:10:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| f8071852-2105-34a7-98e9-eceeb658b894 | -11.7742 | -43.5245 | 2026-10-08 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 362.8 |
| 6b9d76ab-5c60-32f9-accb-a0cd2216328c | -2.4623 | -56.0682 | 2026-10-08 18:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 78733f3a-644d-3ad8-9569-dc6cc5b57362 | -5.99 | -40.97 | 2026-10-08 18:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 006ab58f-d2ef-3b72-95b4-e02f453bf870 | -5.08 | -46.19 | 2026-10-08 18:15:00 | MSG-03 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 883a5eed-c89d-3d22-9279-865cad697967 | -5.37 | -44.22 | 2026-10-08 18:15:00 | MSG-03 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7da38a92-e6ce-310f-ac53-b1719dbe2e48 | -12.22 | -44.84 | 2026-10-08 18:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 36b4ff44-66eb-38f2-8750-fe5cc4765fb6 | -6.07 | -42.61 | 2026-10-08 18:15:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 13968a37-bef9-3e23-9879-a7f6f5333fa3 | -5.97 | -40.93 | 2026-10-08 18:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e2536771-fbaf-375a-858a-d9cafaa9a455 | -13.14 | -54.33 | 2026-10-08 18:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 013fc8b4-c8f7-33c3-9e31-2efb076513c1 | -5.99 | -40.93 | 2026-10-08 18:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a83b70c7-daef-340e-ba28-26319fdb926e | -6.05 | -42.6 | 2026-10-08 18:15:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5c32533e-9604-3d0a-835a-1cab7db1fcf3 | -13.17 | -54.35 | 2026-10-08 18:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4af280c-a8f0-315e-8349-cb61a2c0450b | -13.17 | -54.28 | 2026-10-08 18:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 155c4688-219a-3cda-83f4-2a1d1103c075 | -4.64 | -50.97 | 2026-10-08 18:15:00 | MSG-03 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23ffc1cb-5067-3a95-a993-9ca64001d75f | -6.0 | -41.01 | 2026-10-08 18:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a5094cf6-3daf-3609-98da-ef9f31481365 | -6.0 | -41.06 | 2026-10-08 18:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 63f736d3-29fa-3903-84a5-748500abdaa7 | -4.64 | -50.91 | 2026-10-08 18:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| caeeebff-09d7-39e6-9695-eb051ab50542 | -3.56 | -54.67 | 2026-10-08 18:15:00 | MSG-03 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84955212-ef49-3075-854d-d7237c6e46e7 | -3.84 | -44.11 | 2026-10-08 18:15:00 | MSG-03 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0c6f012-28af-3b9c-9f7b-57b4ac34dbc2 | -3.08 | -53.93 | 2026-10-08 18:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1ec852-3e42-34cd-8987-7051a6b4115b | -2.07 | -46.57 | 2026-10-08 18:15:00 | MSG-03 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63ad75db-fde1-3b83-a6c9-f1f1ebef26f7 | -6.02 | -40.93 | 2026-10-08 18:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef204269-0a86-3fb2-bd59-98ef4e6c579e | -11.08 | -44.08 | 2026-10-08 18:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f287243-ae84-3e03-b51b-89d86c7cc458 | -12.22 | -44.79 | 2026-10-08 18:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ef444ef-593e-323d-a457-0da8ab228287 | -5.11 | -46.24 | 2026-10-08 18:15:00 | MSG-03 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63ba5d41-c984-3beb-98ae-dbac7941423e | -5.11 | -46.19 | 2026-10-08 18:15:00 | MSG-03 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9769f775-3835-3eaf-b5ec-558c975dec4f | -2.1 | -46.57 | 2026-10-08 18:15:00 | MSG-03 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6efcf4c6-6f8d-3469-9851-5bcc8a82e15c | -3.0192 | -53.887 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 767707c2-3fc0-30fe-b5ea-bdce806e0082 | -12.834 | -44.4362 | 2026-10-08 18:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 7e82e80c-a084-3b0b-8c15-06a53905065e | -2.572 | -56.1842 | 2026-10-08 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 452.6 |
| 0221405a-3c0c-3977-a8b8-a656639d5457 | -3.724 | -57.0993 | 2026-10-08 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 10dafb99-6ae4-35fe-8a4e-602036e4e415 | -3.2945 | -54.0006 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| e1879b1f-2fb0-3027-9395-05c0c9ce4da1 | -3.6603 | -54.512 | 2026-10-08 18:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 2bc94500-d0b2-36bd-969a-14de183b5f91 | -9.5003 | -66.8017 | 2026-10-08 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| c1192f69-b8bd-3f08-881c-e4564527c863 | -14.4345 | -43.9157 | 2026-10-08 18:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 273.7 |
| 8a9f97b5-371c-3697-a199-a898bcc483b1 | -10.9766 | -45.3865 | 2026-10-08 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 08df643b-ca96-3dc2-a8f1-4de91aac9b36 | -1.2728 | -55.4135 | 2026-10-08 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 509a416a-5976-3adb-8586-63f4197c8b08 | -8.0766 | -45.6112 | 2026-10-08 18:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 6e30205d-0382-35b9-b075-0284b7baf995 | -8.537 | -66.9764 | 2026-10-08 18:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 1bda0b25-2fb9-358c-b719-cc6eb4ce68f1 | -11.2849 | -45.2063 | 2026-10-08 18:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 4ac08c92-c3fe-3173-acd0-55319e2447ef | -5.6935 | -53.4464 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 5e2f778d-1cc0-32e8-8e45-68a356aefe37 | -5.2853 | -48.1053 | 2026-10-08 18:20:00 | GOES-19 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 20c43c03-b441-3e46-b041-152f8209ae30 | -2.4806 | -56.0875 | 2026-10-08 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 6348981c-17ad-3f22-8dc9-66bbe043b8bc | -6.895 | -43.7066 | 2026-10-08 18:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 220.2 |
| f4f4e205-98ae-3433-86ce-ef41693ebb1f | -7.1827 | -52.6078 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| f9206641-cdac-38f1-851d-c6c4f5646e5b | -7.5847 | -55.7205 | 2026-10-08 18:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| eb5f3a38-424a-33a2-b741-92b16eca198c | -7.0892 | -52.6753 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 233.0 |
| ddbcf9e4-3bcd-3b90-a2bd-f4fb8e37625f | -3.1874 | -58.8358 | 2026-10-08 18:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 9b199f34-2fb1-3299-94ed-e72c68524460 | -6.2342 | -52.8685 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 216.0 |
| 21677b69-9636-3ac2-9fde-d58d4e6f49cd | -2.9265 | -54.1305 | 2026-10-08 18:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| e53c2bd9-0269-396e-bc37-5acc0942e45a | -14.0472 | -43.8222 | 2026-10-08 18:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 300.6 |
| f740f1f2-31fd-31bf-9dd7-55e03b9ecb97 | -2.9265 | -54.1104 | 2026-10-08 18:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| a567ae11-beea-3ecd-98f5-31b3c6fff79f | -2.4805 | -56.1072 | 2026-10-08 18:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 0c5578a2-8c6b-37e6-bd7d-a876385a9ffe | -3.4095 | -58.0013 | 2026-10-08 18:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 4724c941-1552-3cfe-a4a8-3706d03bb08a | -4.6641 | -56.2281 | 2026-10-08 18:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 15ab8223-d28e-358c-aa48-52a1ba229250 | -9.1253 | -67.9432 | 2026-10-08 18:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| ffd48de5-c94f-3994-888d-47446c233eb4 | -3.2214 | -53.8818 | 2026-10-08 18:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 28a17841-3e06-3e0e-9fb0-018a7b1fea9f | -7.4886 | -42.8295 | 2026-10-08 18:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 546ad2af-9c6a-39e2-a1dc-be386332b158 | -6.4392 | -52.7138 | 2026-10-08 18:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 0113e345-ba26-3ebd-8562-86709117bc8e | -7.2372 | -55.0805 | 2026-10-08 18:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 23299098-dc45-36b4-a37f-529074103b8d | -11.7742 | -43.5245 | 2026-10-08 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 65d4313b-c1dc-34e1-921d-2e00da51a4eb | -3.5181 | -41.948 | 2026-10-08 18:20:00 | GOES-19 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |


[Clique aqui para ver as próximas entradas](README390.md)
