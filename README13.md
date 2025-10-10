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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88d692c0-ec6b-3f3e-9a1d-d69d618be7e9 | -10.17419 | -44.55 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae68bd05-fcf9-3c1b-8fcb-991f8618cbc1 | -8.17476 | -43.31776 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a0c97c0-3e4b-3c31-9b5c-41977dc59de0 | -12.6367 | -45.05558 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5b4bbc15-7fb3-379d-9a15-d721046a07db | -7.40487 | -45.9246 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dbf0d561-f27b-3d39-9550-c79331007ee1 | -7.42115 | -42.9772 | 2025-10-10 03:40:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 68fb2aec-8a80-33c9-be31-477caea852ef | -6.45809 | -44.58567 | 2025-10-10 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8247fe84-d3e7-33b0-9424-69babfbe8ac9 | -10.16338 | -44.60711 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 08e45bda-e010-3cb5-bfef-134655acae92 | -12.43333 | -45.77752 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdc0adc7-028f-3665-9b0a-3c46a0ef1c3e | -12.77263 | -45.78234 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28b2c276-b6ae-3e15-8951-89db8b58b83b | -7.40586 | -45.9192 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 65a1137d-6029-3b15-b0ee-f1e2ad68c089 | -7.26195 | -44.91524 | 2025-10-10 03:40:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfa9c715-08cf-39ad-bc1b-cb616b819f29 | -12.43003 | -45.76355 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 614ff75e-eb80-360e-9fda-483792fc4ab6 | -7.66456 | -42.58466 | 2025-10-10 03:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 46e13085-7bdb-3eef-bf93-11f83ff65052 | -7.86028 | -44.45579 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 352a2038-5790-3bc2-9826-17a5905c7494 | -6.75532 | -42.82839 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f07228f9-d94e-3623-84a3-499e81689b0c | -7.39663 | -45.17141 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c11a50b0-4a57-350a-8791-3dace92d4776 | -8.00265 | -44.45632 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c62ea97-919c-3f89-87d8-168add689b9d | -6.75658 | -42.83965 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 06ae081e-94c4-339d-9730-45ad5cc224a2 | -10.16257 | -44.61137 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35a065a3-e7c5-3781-88dd-357cb383898f | -7.41758 | -45.16054 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b454957-6af5-308b-8173-37d818dd0cdd | -9.65987 | -43.8516 | 2025-10-10 03:40:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 93e0fa21-8885-303a-b726-2f66f02f190d | -7.41678 | -45.16496 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c83eab4c-3b0a-31cd-aec3-ef8494d1fb19 | -8.51041 | -46.14656 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac43299b-7407-3697-8164-5e1e73e1cd33 | -6.73698 | -42.80785 | 2025-10-10 03:40:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f729b3a2-ded2-3204-829a-90e5ef6610f8 | -7.77327 | -44.05138 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71e7f61a-2947-3b6b-b0bd-d177ae691751 | -11.4645 | -41.89389 | 2025-10-10 03:40:00 | NPP-375D | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 35147a4b-e7d5-3155-993b-e9e85674c379 | -8.5158 | -46.15301 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d93cc51-2f00-3d16-ae67-62a032473c4c | -6.75826 | -42.84299 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| eb682f30-d529-314d-bb8a-8870c8eda385 | -8.00752 | -44.46236 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0287ef7-4b7e-3c5f-bcd7-47f32d40c848 | -10.17202 | -44.56144 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a86e7fae-9e0d-3e0a-818c-aba0d1b8c52b | -12.62886 | -45.06602 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1033d714-c142-3f9a-8978-ab95858005ab | -11.78777 | -45.04779 | 2025-10-10 03:40:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0504b627-ec53-3cd4-8ace-d8b8c15fef5b | -7.14722 | -42.1893 | 2025-10-10 03:40:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 61a44df8-1df4-3b66-8909-e078a1479aa0 | -7.53583 | -44.30766 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c4c421c-4a54-31b4-9dbf-9e48ce8c6629 | -7.78467 | -44.05307 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f46e650-ae1d-3da8-bc94-a6d39181add1 | -10.15864 | -44.60129 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| cb97e702-7a21-32ad-8416-e76140da8692 | -13.01172 | -41.42614 | 2025-10-10 03:40:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 17486821-a3d5-3503-a454-b626800d4d5e | -5.9314 | -44.06319 | 2025-10-10 03:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68ab5a63-a255-3ed6-8134-9a26e2b181c9 | -7.28822 | -41.97092 | 2025-10-10 03:40:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e422fc23-cbeb-3a3e-a95f-567e0e615031 | -7.27726 | -41.97486 | 2025-10-10 03:40:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 45c4e556-9c28-3c52-b8f8-b7393e4ccb0a | -7.79466 | -44.19214 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a366414f-f92d-3808-941e-87a0df4f673a | -12.74381 | -45.86407 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3ededb6-26a3-3847-8a49-eb343bdaf697 | -13.06408 | -43.8398 | 2025-10-10 03:40:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0939a27c-2b10-3abd-a7c5-37187ce5d4ca | -8.51129 | -46.18351 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 037a2d1c-a53d-3766-b864-e88cb93557d6 | -7.7953 | -42.60243 | 2025-10-10 03:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 56662db5-15a4-3bc2-b96e-0c974373cabe | -10.81976 | -42.82177 | 2025-10-10 03:40:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 075cab12-a661-3dcb-92a4-749a48c0153a | -12.63746 | -45.05175 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 80dad413-4ecd-3f92-a4ca-fc90ea487718 | -5.98037 | -45.9207 | 2025-10-10 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08edd4a9-74ab-3d73-8f6e-740dd49d1505 | -7.41188 | -45.92373 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5bbb23e8-bbff-38ea-9e9d-ca1bac54ed34 | -11.68338 | -47.51945 | 2025-10-10 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e21881a-607f-39f4-9370-1e8ce4c2e47a | -7.76829 | -44.04663 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7de574b0-5524-34d2-807c-1f5a976bc22d | -10.15938 | -44.59737 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b0cd8f94-bd57-3aeb-b29e-14ff9b450679 | -7.5762 | -44.38253 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 716ffea6-0757-3865-b954-68a27befa79e | -8.49913 | -46.20654 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 766ec2dc-939d-335e-8bb0-ade3e259288c | -6.45968 | -44.57668 | 2025-10-10 03:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6903c383-8abb-33d4-8b53-16b466743cfa | -7.79966 | -42.42063 | 2025-10-10 03:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b48060fe-d5e9-3d43-b0ef-cf5c38621617 | -8.84325 | -46.05859 | 2025-10-10 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dc2390c-4f4a-3581-8edf-5fefb09df56d | -12.77926 | -45.77944 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc571cad-0e41-3c15-8742-144253b0a58a | -7.67521 | -42.57638 | 2025-10-10 03:40:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24919f81-b490-3d95-a0cc-bdddf43d8672 | -5.98558 | -45.92078 | 2025-10-10 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f291007c-568a-3e03-9f86-3b2b82d08e6d | -11.68115 | -47.5197 | 2025-10-10 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c724094a-6422-39dd-93c9-d507f0e11cb6 | -10.76892 | -42.68381 | 2025-10-10 03:40:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ca84f4bd-aed3-3c7f-a413-1b6507150bbc | -8.18727 | -43.32695 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3b79bc48-0aae-37f4-95bd-365c7166e175 | -12.6319 | -45.05069 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 952e8fe4-1ff2-36f3-8e94-2210dd424449 | -12.62809 | -45.06992 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 52ba679f-6115-3aa5-8d4f-6033607ed4f6 | -7.41645 | -42.97288 | 2025-10-10 03:40:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 72ae84f7-7e86-3683-8ffa-80e1695bb6c2 | -7.40236 | -39.79105 | 2025-10-10 03:40:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 32304984-ee87-3f91-87d5-5ce43cc0d20f | -7.66346 | -35.15302 | 2025-10-10 03:40:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2e55862b-83a7-33b8-bef6-a989e322d380 | -8.51779 | -46.18414 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 98ab2cc6-7a32-3fdc-9f78-351074bc8744 | -8.00096 | -44.46541 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78b48729-5090-33ac-a790-af51464215d5 | -7.78323 | -44.06097 | 2025-10-10 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a4ef6cc-8d02-3497-9ee7-674b812acac6 | -10.16636 | -44.59135 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bccfc78-d7e2-3e67-b4cb-9ef483feca89 | -7.8429 | -44.5516 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb8ce16e-227f-3ba0-bd98-cd8854a0b4a4 | -11.63733 | -47.53311 | 2025-10-10 03:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d77c2c5c-c511-3593-a7c4-b67529654037 | -8.84036 | -46.06293 | 2025-10-10 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 559fe8c4-cc37-3488-bb63-47e86da86283 | -13.38393 | -42.71487 | 2025-10-10 03:40:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1a061fa8-2ecd-3526-be3c-28a0bb9a7d4c | -7.42588 | -42.98138 | 2025-10-10 03:40:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4928ea6e-5f42-3493-b953-02f6576a0492 | -8.04223 | -43.91318 | 2025-10-10 03:40:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 621b1456-2c8c-3927-b669-5085bbf4a342 | -7.40452 | -45.161 | 2025-10-10 03:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51bc1270-30ed-3bec-90e1-34b8fb5f1847 | -11.46363 | -41.89876 | 2025-10-10 03:40:00 | NPP-375D | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f530005f-4fe8-306f-9310-e3126d724f56 | -7.4055 | -45.9224 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a5f346d8-fe01-3df1-80eb-5606c52a860b | -7.76915 | -42.41511 | 2025-10-10 03:40:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ea8ee2a8-ebea-301c-bde0-47c6332b2454 | -8.00668 | -44.46685 | 2025-10-10 03:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2f02541-ff7d-325a-ad10-5b78c22b2b38 | -8.20714 | -43.38291 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 61631cf6-3462-3632-8e48-0a514ede16ce | -11.53288 | -47.10049 | 2025-10-10 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 300ac583-8e2c-3904-a464-88f28384ba7f | -12.63821 | -45.04793 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 551a80c6-e386-3423-81f8-077cc811b80e | -8.89795 | -46.01233 | 2025-10-10 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 122faedb-2525-3260-987a-1ce80e7b3a47 | -10.25864 | -37.86733 | 2025-10-10 03:40:00 | NPP-375D | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0018bcc-853d-32db-8278-6cc988aee431 | -7.08087 | -43.51489 | 2025-10-10 03:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d18f02f-81c4-3b36-b10c-5da82e661c2d | -6.6281 | -39.30795 | 2025-10-10 03:40:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 024541fc-94cc-3f82-b02b-d1c05fd24b5e | -7.0794 | -43.51799 | 2025-10-10 03:40:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af0f1b61-0071-3eae-afa8-f517d6f03f89 | -7.40649 | -45.91716 | 2025-10-10 03:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12cca62c-0d8b-3743-aab3-cd558006d22a | -5.64301 | -45.96888 | 2025-10-10 03:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfb83d69-1c68-3cd9-99e0-a05e869dc59c | -12.77348 | -45.77822 | 2025-10-10 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd1c3815-dc2f-34c8-bef5-7bb67892896a | -6.73574 | -42.84612 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cf531c81-cb1a-3344-84f7-4137507c89e5 | -10.16649 | -44.55992 | 2025-10-10 03:40:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5430a8dd-b263-36eb-9887-d867cbe6549a | -8.1836 | -43.32986 | 2025-10-10 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8aaae4f6-b03d-368f-81cd-53856881cf9d | -11.9693 | -45.22086 | 2025-10-10 03:40:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66a0d167-066e-3f4d-9fad-4fa54501ff92 | -7.79362 | -42.61168 | 2025-10-10 03:40:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb848394-4fbd-3217-9974-5f8fdbc33a58 | -6.75294 | -42.84201 | 2025-10-10 03:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |


[Clique aqui para ver as próximas entradas](README14.md)
