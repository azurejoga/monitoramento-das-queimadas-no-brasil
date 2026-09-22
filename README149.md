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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53780388-5f14-32a4-92fc-8a7ccec7bca8 | -7.5548 | -48.6843 | 2026-09-22 15:20:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 8e98e728-6586-311a-a87f-aeaa4ab07a8e | -6.0926 | -57.6652 | 2026-09-22 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 25cadcc1-8f78-3edf-8e32-eb519420ad2a | -6.728 | -59.423 | 2026-09-22 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 575ea222-9c79-3955-963f-3ac23efee747 | -2.9723 | -57.214 | 2026-09-22 15:20:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 4b4fd156-6a88-34ae-b802-dc56e55d81e6 | -8.7706 | -45.8567 | 2026-09-22 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| dcc0226f-4bc1-3541-a51f-9ae71e7170bc | -10.7251 | -50.7896 | 2026-09-22 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 488868c4-33ae-3f15-9993-9c480de4af80 | -2.9525 | -57.72 | 2026-09-22 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| b088c682-5c2b-303e-8c54-4df8efa26ef0 | -3.2955 | -59.4284 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 151b8805-d8d8-3041-8dce-2db6f4af514c | -3.6447 | -58.9224 | 2026-09-22 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| f2402ac1-7fe4-34f6-9f36-6220f768e6ff | 1.2608 | -50.976 | 2026-09-22 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f056f286-c448-3618-8a93-bf8fd64368e5 | -3.4215 | -60.1896 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| bbc5d0e6-21f5-3bc8-94cb-dfb6c3cf8c7f | -10.8002 | -50.8243 | 2026-09-22 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e21d94c7-92b4-3c9e-903b-c73a75ce0af5 | 3.9315 | -60.8633 | 2026-09-22 15:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 5b4554ac-43f8-3568-b268-16da36004bf7 | -3.1358 | -57.6775 | 2026-09-22 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| fbb236b3-bd37-3afa-a7ce-74b0e073f176 | -7.0029 | -49.7551 | 2026-09-22 15:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4419fec1-3a76-3415-a255-820c2c702b9e | -2.5492 | -58.0179 | 2026-09-22 15:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 83251086-aded-3d6c-ad78-f1c3d14d1c2b | -12.8906 | -50.9267 | 2026-09-22 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 2d5cb532-fdeb-35b4-b499-707b1ab60264 | -3.1278 | -60.6889 | 2026-09-22 15:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a6c1a83f-a840-3fca-8bba-580e86a769ca | -10.336 | -50.2119 | 2026-09-22 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4a31df5a-d7d5-30cc-b7b2-54bd2b8c8eec | -5.6223 | -43.3701 | 2026-09-22 15:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 324f14fe-65d6-343c-8cf0-1099ce782d5b | -5.8593 | -53.5399 | 2026-09-22 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 63aa3511-5fa9-37ea-a2ee-78e3bd9b80b8 | -14.6688 | -45.6565 | 2026-09-22 15:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 425.6 |
| 282e752d-7b4a-3db2-b483-c7bba8c76541 | -3.5528 | -59.0397 | 2026-09-22 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f50ba908-a0c9-31c7-a7b1-505777a4e6c9 | 2.2187 | -50.8769 | 2026-09-22 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a994337c-c925-3784-8034-ee742f7a5fff | -3.4272 | -58.1945 | 2026-09-22 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 27fc8ea1-0fa9-3e34-b2aa-103a073a829a | -6.0925 | -57.6847 | 2026-09-22 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 184.8 |
| d834eb91-a1a6-37c2-ba59-cac2b3b3b65a | 2.4396 | -50.9552 | 2026-09-22 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b7e729cd-a96d-3a84-8984-3906fc291f2c | -3.132 | -59.0482 | 2026-09-22 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 43008035-bb51-3983-beaa-cf0a79ff60d9 | -6.2765 | -47.585 | 2026-09-22 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ee9ae475-c205-3889-b700-13b4066be4b3 | -3.2182 | -61.0661 | 2026-09-22 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 9a40992c-07a5-3343-83ad-d233949cba73 | -7.1392 | -42.0811 | 2026-09-22 15:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 153.9 |
| 9ff456f3-9f07-3361-908a-d50cd366b115 | 1.5836 | -55.7856 | 2026-09-22 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b3b6d1c7-d902-3622-8980-607e3749ce07 | -10.6889 | -50.6658 | 2026-09-22 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| e734aa5e-315e-3042-841f-d8da10865d5c | -3.6449 | -58.8647 | 2026-09-22 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 037deb2e-fafa-35a3-bf51-4ed028bcf467 | -6.183 | -47.6133 | 2026-09-22 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 681b2e86-f3a6-3bc4-8ad6-d1169e000a54 | -3.1514 | -58.644 | 2026-09-22 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 8e658d48-c28c-3e67-a4ca-f2a13616b755 | -11.4527 | -50.2409 | 2026-09-22 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 79d2bc3d-0296-3ca3-ba44-0adad620577b | -5.9148 | -53.5372 | 2026-09-22 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| d129caa9-54db-33b9-86e1-2c798a10485e | -5.8489 | -49.7875 | 2026-09-22 15:20:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f90d0f21-32ae-3e8e-bf56-ad431b9ddf3a | -6.4671 | -59.9711 | 2026-09-22 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 80acd18f-6e98-3b19-94ee-a9ab8800dd18 | -2.4023 | -58.2715 | 2026-09-22 15:20:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 5d79cb20-c4fa-3212-8a96-1e9de85d9787 | -12.283 | -50.7011 | 2026-09-22 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| e00b0124-537b-3863-84e2-fba748945442 | -3.3 | -57.8681 | 2026-09-22 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 06d72d8f-6f4e-3961-bf16-cda2ecd496be | -10.4486 | -50.2644 | 2026-09-22 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 101c66eb-4137-3569-9f6c-8c1f75a18f2f | -10.6688 | -50.7529 | 2026-09-22 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 60a8b0ec-2e67-3b45-a98e-ff32bb3b3ea7 | -2.8534 | -60.9206 | 2026-09-22 15:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c5fa932c-b293-3ce3-9ad6-c225622cc2d3 | -12.2834 | -50.6797 | 2026-09-22 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e18e7c09-0e88-3046-ad23-98ec9afd41fc | -6.7463 | -59.4416 | 2026-09-22 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 431f9d8f-0e1a-335b-b28d-36e7f12d3022 | -9.2468 | -57.1686 | 2026-09-22 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| cbf8003e-edfc-3fd6-b09c-20ab79823784 | -3.6065 | -59.4413 | 2026-09-22 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 9233aad4-4990-38de-8b74-65a269f6c65c | -3.2183 | -61.0472 | 2026-09-22 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 436fe96f-0d21-3b0d-8f5c-e9373011b9e1 | 2.7086 | -60.2969 | 2026-09-22 15:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 456c550b-f70b-328b-9987-055387fff957 | -3.0535 | -61.2578 | 2026-09-22 15:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 08841737-36c0-3eb1-8646-8d8ae016e3bf | -3.2955 | -59.4476 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| b2d441a0-73a9-3f2e-a7e2-c4af733789a1 | -3.331 | -59.8483 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 95fd25f5-7ddf-320f-9057-d2da4e9dd13b | -6.2761 | -47.6287 | 2026-09-22 15:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0162c07b-41d9-38c0-aa19-c4fd4fe0b234 | -6.9849 | -59.663 | 2026-09-22 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| a8e396e9-4740-348b-8385-7f1c75f58224 | -10.7807 | -50.8688 | 2026-09-22 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 87b5297a-5464-35fe-bd37-b58e35bdb6f9 | -3.4214 | -60.2086 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1eb81b4f-2219-3d81-b573-f171228f0c84 | -6.3501 | -57.7717 | 2026-09-22 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| da741029-5ada-362b-bd99-e4086007fb1e | -9.8404 | -46.3911 | 2026-09-22 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 26511926-3ff6-3896-9831-842dd0483027 | -9.1057 | -60.9511 | 2026-09-22 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| fc5624dd-eaa7-31ed-8b20-0d31f89c640b | -3.2211 | -53.9623 | 2026-09-22 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 7e8ae031-4136-3c0d-8e4c-969e923a09a6 | -3.2818 | -57.8491 | 2026-09-22 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 18068622-610b-3182-ac94-58433476806c | 2.9283 | -60.0651 | 2026-09-22 15:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6f79ed5e-cd90-3f9f-9322-eab976d57bee | -3.6813 | -58.9216 | 2026-09-22 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 77f1949b-dd19-308d-a2ec-062f39f48545 | -10.3168 | -50.2352 | 2026-09-22 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 774de593-b7a3-3d22-b952-028a0edd0d60 | 4.1314 | -61.3134 | 2026-09-22 15:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 06110783-e1c5-3da5-86d1-a85e53924506 | -3.2817 | -57.8685 | 2026-09-22 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| bb3914f8-aea1-3467-bcac-c71514f91594 | -5.9335 | -59.9515 | 2026-09-22 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| b354696d-a9dd-3053-8d37-68f6d5680ed1 | 3.9354 | -59.6063 | 2026-09-22 15:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 42aeea8b-29f2-3f9e-ac66-1e918026af6d | -2.5687 | -57.5135 | 2026-09-22 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 90.3 |
| f34e337a-45bd-359f-94a2-a1e62020bc7f | -6.2394 | -41.6875 | 2026-09-22 15:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 7acd27c5-29b9-3ebc-a151-5ea33e3b0b92 | -3.1719 | -57.832 | 2026-09-22 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| c45a2113-dbc1-3f56-b71d-f4145f67b272 | -7.5705 | -57.657 | 2026-09-22 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 1d348593-1c78-3181-bbd1-a7d000d5e1ee | -10.9547 | -50.5952 | 2026-09-22 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 2d728875-bbfe-38a6-b47b-901c857cfbe4 | -7.6942 | -61.5473 | 2026-09-22 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| ec1f198a-8323-35a0-aafc-cf81d0f503aa | -9.257 | -46.1873 | 2026-09-22 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| b736ea37-f0d7-3143-a163-3e01b668b450 | -8.3777 | -45.6263 | 2026-09-22 15:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 122.0 |
| c8c76f8d-7870-3c59-af47-f5ec0d23e86a | -5.4179 | -60.2166 | 2026-09-22 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 840cd677-cea7-3f86-b558-a50b6474e54a | -3.6997 | -58.9019 | 2026-09-22 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 6ba40638-b2bd-36d2-a27f-e4af70b69b09 | -5.8239 | -43.8656 | 2026-09-22 15:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 5af69b3d-2455-30a8-903d-9ec46259de18 | -3.3322 | -59.3894 | 2026-09-22 15:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 49b4cf61-5183-3508-a6a1-dcf558cc3f87 | -10.744 | -50.7876 | 2026-09-22 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 8834390e-3700-34d0-ba07-9bd2136cd243 | -11.3976 | -44.2167 | 2026-09-22 15:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 276.6 |
| e035de45-18b0-390c-a483-dcd9ad76f433 | 1.9056 | -50.8414 | 2026-09-22 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 57.1 |
| dda59f92-7b7a-3b7e-a11d-e5a11aed12d0 | 3.7879 | -59.9535 | 2026-09-22 15:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 54cf3065-56b7-3f33-b774-ff85c17bca58 | -3.4634 | -58.329 | 2026-09-22 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 3e5582d5-da28-3f6c-be44-42550013151b | -3.4003 | -61.2898 | 2026-09-22 15:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| a6326e72-3e32-3cf8-876f-ccf0838e0515 | -3.6264 | -58.9228 | 2026-09-22 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c758a4b1-d9a2-3677-aa2b-3bbeb54bbf29 | -3.6763 | -60.5839 | 2026-09-22 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| cef9032c-ecec-33e3-a3c4-ead7634933f8 | 2.2923 | -50.9377 | 2026-09-22 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 671df756-6064-35f1-b7c0-1a6b0544b0d5 | -5.4363 | -60.2161 | 2026-09-22 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 00f3a35e-c34f-3354-93c9-012fbde21955 | -3.7364 | -58.8818 | 2026-09-22 15:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6501b398-a696-35f8-bc66-0c90d465b46b | 1.968 | -55.8989 | 2026-09-22 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e0991d1e-1ddc-356a-80b3-63d9d69721b5 | -7.7144 | -61.2419 | 2026-09-22 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 6430d78b-b3cc-3718-8a6e-9474d8b8c288 | -8.6173 | -54.5924 | 2026-09-22 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 90433f7a-d453-344f-a293-a7987118c312 | 4.0579 | -61.4095 | 2026-09-22 15:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| fa6e914d-2ae8-366b-8a05-d3b52599b670 | -6.3842 | -55.265 | 2026-09-22 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 934ad520-4454-3564-a16c-a8977bac1480 | -3.6947 | -60.5455 | 2026-09-22 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |


[Clique aqui para ver as próximas entradas](README150.md)
